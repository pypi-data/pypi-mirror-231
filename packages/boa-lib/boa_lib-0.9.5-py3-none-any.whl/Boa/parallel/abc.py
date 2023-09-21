"""
This module defines some Abstract Base Classes used by the parallel package.
"""

from abc import ABCMeta, abstractmethod
from collections import deque
from threading import Event, Lock, RLock
from typing import (Callable, Generator, Generic, Iterable, Iterator,
                    ParamSpec, Protocol, TypeVar)
from weakref import WeakSet, ref

__all__ = ["Future", "Worker"]





P = ParamSpec("P")
R = TypeVar("R")
T = TypeVar("T")
Y = TypeVar("Y")

class Future(Generic[T], metaclass = ABCMeta):

    """
    A Future represents an eventual value. This value might get defined at some point but it can also be set to raise an exception.
    You can wait for it like an Event. Contrary to an Event, you cannot set it twice without clearing it (raises FutureSetError).
    To avoid waiting forever, it is good to raise an UnreachableFuture exception when you know a Future will never come.
    """

    from threading import RLock as __RLock
    from weakref import WeakSet as __WeakSet

    from .exceptions import CancelledFuture as __CancelledFuture

    __slots__ = {
        "__linked" : "The set of Futures directly linked to this particular Future.",
        "__group" : "The set of Futures linked directly or not to this particular Future.",
        "__group_lock" : "A lock used to iterate over the group of causally equivalent Futures.",
        "__weakref__" : "A placeholder for weak references."
    }

    __linking_lock = RLock()

    def __init__(self):
        self.__linked : "set[Future[T]]" = set()
        self.__group : "WeakSet[Future[T]]" = self.__WeakSet((self, ))
        self.__group_lock = self.__RLock()

    def __repr__(self) -> str:
        """
        Implements repr(self).
        """
        return f"<{type(self).__name__} at {hex(id(self))}: {('cancelled' if self.cancelled else 'errored' if self.exception is not None else 'set') if self.is_set else 'unset'}>"

    @abstractmethod
    def set(self, value : T) -> None:
        """
        Sets the value of the Future. The Future must not be already set.
        It may raise ExceptionGroups if errors occur while propagating causality.
        """
        raise NotImplementedError

    @abstractmethod
    def set_exception(self, exc : BaseException) -> None:
        """
        Makes the Future raise an exception. The Future must not be already set.
        It may raise ExceptionGroups if errors occur while propagating causality.
        """
        raise NotImplementedError
    
    @property
    @abstractmethod
    def is_set(self) -> bool:
        """
        Indicates if the Future has been set.
        """
        raise NotImplementedError
    
    @property
    @abstractmethod
    def value(self) -> T | None:
        """
        The current value of the Future.
        Raises FutureUnsetError if the Future is not set.
        Returns None if the Future had an exception.
        """
        raise NotImplementedError
        
    @value.setter
    def value(self, value : T):
        """
        Sets the Future to a value. Equivalent to self.set(value).
        """
        self.set(value)

    @value.deleter
    def value(self):
        """
        Resets the Future. Equivalent to self.clear().
        """
        self.clear()
    
    @property
    @abstractmethod
    def exception(self) -> BaseException | None:
        """
        The current exception raised by the Future.
        Raises FutureUnsetError if the Future is not set.
        Returns None if the Future did not have an exception.
        """
        raise NotImplementedError
        
    @exception.setter
    def exception(self, value : BaseException):
        """
        Sets the exception of the Future. Equivalent to self.set_exception(value).
        """
        if not isinstance(value, BaseException):
            raise TypeError(f"Expected BaseException, got '{type(value).__name__}'")
        self.set_exception(value)
    
    @exception.deleter
    def exception(self):
        """
        Resets the Future. Equivalent to self.clear().
        """
        self.clear()

    @property
    @abstractmethod
    def cancelled(self) -> bool:
        """
        Indicates if the Future has been cancelled.
        """
        raise NotImplementedError
    
    @cancelled.setter
    def cancelled(self, value : bool):
        """
        Sets the cancel state of the Future.
        Setting to True is equivalent to self.cancel().
        Setting to False is equivalent to self.clear().
        """
        if not isinstance(value, bool):
            raise TypeError(f"Expected bool, got '{type(value).__name__}'")
        if value:
            self.cancel()
        else:
            self.clear()

    @abstractmethod
    def add_callback(self, cb : Callable[["Future[T]"], None]):
        """
        Adds a callback for the realization of the Future. It will be called with the Future object as argument each time it realizes or there is an exception.
        Note that adding a callback when the Future is already set will cause it to be called immediately.
        """
        raise NotImplementedError

    @abstractmethod
    def remove_callback(self, cb : Callable[["Future[T]"], None]):
        """
        Removes all instances of the given callback.
        """
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> None:
        """
        Clears the Future. Removes the associated value and exception.
        """
        raise NotImplementedError

    @abstractmethod
    def wait(self, timeout : float = float("inf")) -> bool:
        """
        Waits for the realization of the Future. Returns a boolean indicating if the Future has been realized.
        If the timeout is given, waits at most for this timeout and returns.
        """
        raise NotImplementedError

    @abstractmethod
    def result(self, timeout : float = float("inf")) -> T:
        """
        Waits for the Future to be resolved and returns the associated value.
        Raises TooFarFutureError if the future has not been resolved before timeout has been reached.
        """
        raise NotImplementedError

    def link(self, past : "Future[T]"):
        """
        Links this Future to another. When the other Future realizes, this one will be realized in an identical way.
        Silently does nothing if they were linked.
        """
        if not isinstance(past, type(self)):
            raise TypeError(f"Expected '{type(self).__name__}', got '{type(past).__name__}'")

        with self.__linking_lock, self.__group_lock, past.__group_lock:

            self.__linked.add(past)
            past.__linked.add(self)

            if self.__group is past.__group:
                return

            g = self.__group | past.__group

            self.__group = g
            past.__group = g
            past.__group_lock = self.__group_lock

    def unlink(self, past : "Future[T]"):
        """
        Unlinks this Future from another.
        Silently does nothing if they were not linked.
        """
        if not isinstance(past, type(self)):
            raise TypeError(f"Expected '{type(self).__name__}', got '{type(past).__name__}'")
        
        def explore(fut : "Future[T]") -> "WeakSet[Future[T]]":
            """
            Internal function used to find all the Futures causally connected to a starting Future.
            """
            s = self.__WeakSet({fut})
            new = self.__WeakSet({fut})
            while new:
                new = self.__WeakSet().union(*[f.__linked for f in new]) - s
                s |= new
            return s

        with self.__linking_lock, self.__group_lock, past.__group_lock:

            if self.__group is not past.__group:
                return
            
            self.__linked.discard(past)
            past.__linked.discard(self)

            old_group = self.__group
            g1 = explore(self)
            if len(g1) != len(old_group):       # Then we just cut a group in two subgroups
                g2 = explore(past)
                new_lock = self.__RLock()
                
                if len(g1) > len(g2):           # Change the smallest group
                    for fut in g2:
                        fut.__group = g2
                        fut.__group_lock = new_lock
                    old_group -= g2
                else:
                    for fut in g1:
                        fut.__group = g1
                        fut.__group_lock = new_lock
                    old_group -= g1

    def linked(self) -> "Iterator[Future[T]]":
        """
        Iterates over all the linked Futures. While iterating, a lock is held, preventing iterating simultenously from another Future linked (directly or not) to this one.
        """

        def get_lock(fut : "Future") -> "RLock":
            """
            Just returns the private __group_lock.
            """
            return fut.__group_lock
        
        class LockedIter:

            """
            Internal classs used to keep a lock on a group while iterating of a Future's direct neighbors.
            """

            def __init__(self, fut : "Future[T]", s : "set[Future[T]]") -> None:
                while True:
                    lock = get_lock(fut)
                    lock.acquire()
                    if get_lock(fut) == lock:
                        break
                    lock.release()
                self.__lock = lock
                self.__iter = iter(s.copy())
            
            def __iter__(self):
                """
                Implements iter(self).
                """
                return self
            
            def __next__(self):
                """
                Implements next(self).
                """
                return next(self.__iter)
            
            def __del__(self):
                """
                Implements del self.
                """
                try:
                    self.__lock.release()
                except RuntimeError:
                    pass            # For some reasons, it was not always acquired...


        return LockedIter(self, self.__linked)
    
    def __del__(self):
        """
        Implements del self.
        """
        self.__group.discard(self)
        while self.__group:
            try:
                f = next(iter(self.__group))
                self.unlink(f)
            except StopIteration:
                return
            except:
                pass

    def cancel(self):
        """
        Cancels the execution of the task by raising CancelledFuture.
        """
        self.set_exception(self.__CancelledFuture(self, "Task cancelled"))





class Worker:

    """
    The Worker Protocol describes classes used to start the execution of a task, which returns a Future to the result of the task.
    """

    @abstractmethod
    def execute_async_into(self, fut : Future[R], func : Callable[P, R], *args : P.args, **kwargs : P.kwargs):
        """
        Classes that match the Worker protocol must provide this method to execute a given function and set its result into the given Future.
        """
        raise NotImplementedError
    
    def execute_async(self, func: Callable[P, R], *args: P.args, **kwargs: P.kwargs) -> Future[R]:
        """
        Starts the execution of the given function into the worker and returns a Future to the result of the function.
        """
        from .thread import Future
        fut = Future()
        self.execute_async_into(fut, func, *args, *kwargs)
        return fut

    @abstractmethod
    def kill(self) -> None:
        """
        Classes that match the Worker protocol must provide this method to cancel the execution of a task by killing themselves.
        """
        raise NotImplementedError
    




module_ready = Event()
pool_manager_ready = Event()
W = TypeVar("W", bound=Worker)
class DefaultCallback(Protocol):
    
    """
    This is just a type annotation for a callable that takes an optional Future object as only argument (or no argument).
    """

    def __call__(self, fut : Future | None = None) -> None:
        ...

class Pool(Generic[W], metaclass = ABCMeta):

    """
    This is the abstract base class for Pool objects.
    A Pool represents a set of worker objects that can be used to execute multiple tasks.
    """

    from .exceptions import FutureSetError as __FutureSetError
    from .thread.primitives import DaemonThread as __DaemonThread
    from .thread.synchronization import PLock as __PLock
    from weakref import ref as __ref
    from collections import deque as __deque

    __signaled = Event()
    __signaled_queue : "__deque[__ref[Pool[W]] | __ref[MapIterator]]" = __deque()
    __signal_lock = Lock()

    @staticmethod
    def _signal(object : "Pool[W] | MapIterator"):
        with Pool.__signal_lock:
            if not Pool.__signaled_queue or not any(s() is object for s in Pool.__signaled_queue):        # Useless to signal twice
                Pool.__signaled_queue.append(Pool.__ref(object))
                Pool.__signaled.set()
        


    class MapIterator(Generic[R]):

        """
        A parallel version of builtin map.
        """

        from sys import getsizeof as __getsizeof_init
        __getsizeof = staticmethod(__getsizeof_init)
        del __getsizeof_init
        from .exceptions import FutureSetError as __FutureSetError
        from weakref import ref as __ref
        from threading import RLock as __RLock, Event as __Event
        from collections import deque as __deque

        def __init__(self, pool : "Pool", func : Callable, iter : Iterator[tuple], cachesize : int | None = None, cachelen : int | None = None) -> None:
            self.__pool = pool
            self.__func = func
            self.__iter = iter
            self.__cachesize = cachesize
            self.__cachelen = cachelen
            self.__queue : "deque[Future[R]]" = self.__deque()
            self.__queue_not_empty = self.__Event()
            self.__results_size : "dict[Future[R], int]" = {}
            self.__results_len = 0
            self.__active : "set[Future[R]]" = set()
            self.__lock = self.__RLock()
            self.__exhausted = False

        @property
        def pool(self) -> "Pool":
            """
            Returns the Pool that this MapIterator is attached to.
            """
            return self.__pool

        # Note that there are many static methods here to avoid holding references to MapIterator objects, allowing them to be deleted when they are no longer used, freeing the CPU...

        def __has_cache_space(self) -> bool:
            """
            Internal function used to check if the result cache has enough space to keep submitting tasks to the pool.
            """
            with self.__lock:
                if self.__cachesize is not None:
                    ok1 = sum(self.__results_size.values()) < self.__cachesize
                else:
                    ok1 = True
                if self.__cachelen is not None:
                    ok2 = self.__cachelen < self.__results_len
                else:
                    ok2 = True
                return ok1 and ok2
            
        @property
        def __notify(self) -> DefaultCallback:
            """
            Notifies the Pool scheduler to check the state of this MapIterator.
            It is actually a weak method property used to create a weak callback function (one that does not hold a reference to the instance).
            """
            rself: "ref[Pool.MapIterator[R]]" = self.__ref(self)
            del self

            def notify(fut : "Future[R] | None" = None):
                self = rself()
                if self is not None:
                    with self.__lock:
                        if fut is not None:
                            self.__active.discard(fut)
                            if fut in self.__queue:
                                self.__results_len += 1
                                self.__results_size[fut] = self.__getsizeof(fut.value)
                    if not self.__exhausted:
                        Pool._signal(self)
                
            return notify

        def _adjust_active_tasks(self):
            """
            Internal function used to declare tasks to the pool if some can be declared.
            """
            with self.__lock:
                if self.__exhausted or not self.__has_cache_space():
                    return
                while len(self.__active) < 2 * self.__pool.size:
                    try:
                        next_args = next(self.__iter)
                    except StopIteration:
                        self.__exhausted = True
                        return
                    self.__queue.append(fut := self.__pool.apply_async(self.__func, *next_args))
                    self.__queue_not_empty.set()
                    self.__active.add(fut)
                    fut.add_callback(self.__notify)

        def __iter__(self) -> Iterator[Future[R]]:
            """
            Implements iter(self).
            """
            return self
        
        def __next__(self) -> Future[R]:
            """
            Implements next(self).
            """
            with self.__lock:
                if not self.__queue:
                    if self.__exhausted:
                        raise StopIteration
                    self.__queue_not_empty.clear()
                    self.__notify()

            self.__queue_not_empty.wait()

            with self.__lock:
                fut = self.__queue.popleft()
                if fut in self.__results_size:
                    self.__results_size.pop(fut)
                    self.__results_len -= 1
                return fut
            
        def __del__(self):
            """
            Implements del self.
            """
            excs : list[BaseException] = []
            with self.__lock:
                self.__exhausted = True
                active = self.__active.copy()
                self.__active.clear()
            for fut in active:
                try:
                    fut.cancel()
                except* self.__FutureSetError:
                    pass
                except* BaseException as e:
                    excs.append(e)
            if excs:
                raise BaseExceptionGroup("Some errors occured while cancelling tasks", excs)
                
            


    def __init__(self, maxsize : int) -> None:
        if not isinstance(maxsize, int):
            raise TypeError(f"Expected int, got '{type(maxsize).__name__}'")
        if maxsize <= 0:
            raise ValueError(f"Expected positive nonzero size, got {maxsize}")
        self.__pool : "list[W]" = []
        self.__lock = self.__PLock()
        self.__affectations : "dict[Future, W]" = {}
        self.__pending : "deque[tuple[Future, Callable, tuple, dict]]" = self.__deque()
        self.__maxsize = maxsize
        self.__closed : bool = False
        self.__notify()

    __pool_scheduler_lock = Lock()

    @staticmethod
    def __pool_scheduler():
        """
        Internal function used to schedule the tasks of all the Pools!
        """
        module_ready.wait()
        with Pool.__pool_scheduler_lock:
            pool_manager_ready.set()
            
            del Pool.__pool_scheduler         # Just to ensure it won't be lauched twice!

            while True:

                Pool.__signaled.wait()
                with Pool.__signal_lock:
                    rself = Pool.__signaled_queue.popleft()
                    if not Pool.__signaled_queue:
                        Pool.__signaled.clear()
                assert rself != None, f"Pool scheduler has not received a reference to an object to handle: received a '{type(rself).__name__}'"

                self = rself()

                if isinstance(self, Pool):
                    with self.__lock:
                        if not self.__closed:
                            self.__cleanup_pool()
                            if not self.__adjust_pool():
                                while self.__pending and len(self.__affectations) < self.size:
                                    fut, func, args, kwargs = self.__pending.popleft()
                                    if not fut.cancelled:
                                        chosen_worker = None
                                        for w in self.__pool:
                                            if w not in self.__affectations.values():
                                                chosen_worker = w
                                        if chosen_worker is None:
                                            raise RuntimeError("State of the pool changed while the Pool scheduler was scheduling it")
                                        self.__affectations[fut] = chosen_worker
                                        imediate_fut = chosen_worker.execute_async(func, *args, **kwargs)
                                        imediate_fut.link(fut)
                                        imediate_fut.add_callback(self.__notify)
                
                elif isinstance(self, Pool.MapIterator):
                    self._adjust_active_tasks()

                elif self is None:
                    pass
                
                else:
                    raise RuntimeError(f"Pool scheduler has been signaled to handle a non-Pool related object : received a reference to a '{type(self).__name__}'")
                
                del self

    __DaemonThread(target = __pool_scheduler, name = "Pool Scheduler Thread").start()

    @property
    def __notify(self) -> DefaultCallback:
        """
        Notifies the Pool scheduler to check the state of this Pool.
        It is actually a weak method property used to create a weak callback function (one that does not hold a reference to the instance).
        """
        rself: "ref[Pool[W]]" = self.__ref(self)
        del self

        def notify(fut : "Future | None" = None):
            self = rself()
            if self is not None:
                if fut is not None and fut.cancelled:       # If a task has been cancelled and was affected : kill the worker and remove it
                    with self.__lock:
                        if fut in self.__affectations:
                            w = self.__affectations.pop(fut)
                            w.kill()
                            self.__pool.remove(w)
                Pool._signal(self)
            
        return notify
    
    def __cleanup_pool(self):
        """
        Internal function used to free workers who have finished their tasks.
        """
        with self.__lock:
            for fut in self.__affectations.copy():
                if fut.is_set:
                    self.__affectations.pop(fut)

    def __add_worker(self):
        """
        Internal function used to create a new worker in the background.
        """
        if not self.__closed:
            self.__pool.append(self._spawn())

    def __remove_worker(self, worker : W):
        """
        Internal function used to remove a worker in the background.
        """
        self.__pool.remove(worker)
        worker.kill()
    
    def __adjust_pool(self) -> bool:
        """
        Internal function to spawn missing workers.
        Returns True if there are pending operations on the Pool after the call to this method.
        """
        tasks_pending = False
        with self.__lock:
            missing = self.size - len(self.__pool)
            if missing > 0 and not self.__closed:
                threads = [self.__DaemonThread(target = self.__add_worker, name = f"Worker Spawner #{n}") for n in range(missing)]
                def waiter_1():
                    with self.__lock:
                        for t in threads:
                            t.start()
                        for t in threads:
                            t.join()
                    self.__notify()
                w = self.__DaemonThread(target = waiter_1, name = "Pool Adjuster Notifier")
                self.__lock.pass_on(w)
                w.start()
                tasks_pending = True
            elif missing < 0:
                excess = -missing
                removed = 0
                to_remove : "list[W]" = []
                for w in self.__pool:
                    if w not in self.__affectations.values():
                        to_remove.append(w)
                        removed += 1
                    if removed >= excess:
                        break
                threads = [self.__DaemonThread(target = self.__remove_worker, args = (w, ), name = f"Worker Spawner #{n}") for n, w in enumerate(to_remove)]
                def waiter_2():
                    with self.__lock:
                        for t in threads:
                            t.start()
                        for t in threads:
                            t.join()
                    self.__notify()
                w = self.__DaemonThread(target = waiter_2, name = "Pool Adjuster Notifier")
                self.__lock.pass_on(w)
                w.start()
                tasks_pending = True
            return tasks_pending

    @property
    def size(self) -> int:
        """
        The maximum number of workers that can be in the Pool.
        """
        return self.__maxsize
    
    @size.setter
    def size(self, maxsize : int):
        """
        Sets the size of the pool, starting new workers if possible and tasks are pending.
        Note that reducing the size of the pool might be postponed if all workers are active (just enough will die when they complete their active task).
        """
        if not isinstance(maxsize, int):
            raise TypeError(f"Expected int, got '{type(maxsize).__name__}'")
        if maxsize <= 0:
            raise ValueError(f"Expected positive nonzero size, got {maxsize}")
        with self.__lock:
            if self.__closed:
                raise RuntimeError("Pool is closing")
        self.__maxsize = maxsize
        self.__notify()
        
    def close(self):
        """
        Closes the Pool. Not more task can be submitted.
        """
        self.__closed = True
    
    @property
    def closed(self) -> bool:
        """
        Indicates if the bool has been closed.
        """
        return self.__closed
    
    @closed.setter
    def closed(self, value : bool):
        if not isinstance(value, bool):
            raise TypeError(f"Expected bool, got '{type(value).__name__}'")
        if self.__closed and not value:
            raise ValueError("Cannot re-open a Pool")
        if value:
            self.close()
    
    @classmethod
    @abstractmethod
    def _spawn(cls) -> W:
        """
        Creates a Worker object. Used internally to maintain the worker pool.
        """
        raise NotImplementedError(f"You need to implement the '_spawn' method of the '{cls.__name__}' class")
        
    def __del__(self):
        """
        Implements del self. Kills all the active workers.
        """
        print("Deleting pool...")
        with self.__lock:
            self.close()
            excs : list[BaseException] = []
            for fut, func, args, kwargs in self.__pending:
                try:
                    fut.cancel()
                except* self.__FutureSetError:
                    pass
                except* BaseException as e:
                    excs.append(e)
            for fut in self.__affectations:
                try:
                    fut.cancel()
                except* self.__FutureSetError:
                    pass
                except* BaseException as e:
                    excs.append(e)
            for w in self.__pool:
                w.kill()
            print("Pool deleted!")
            if excs:
                raise BaseExceptionGroup("Some errors occured while cancelling tasks", excs)

    def is_running(self, f : Future) -> bool:
        """
        Returns True if the given Future matches a task that is currently being executed by the pool.
        """
        if not isinstance(f, Future):
            raise TypeError(f"Expected Future, got '{type(f).__name__}'")
        return f in self.__affectations
    
    def is_pending(self, f : Future) -> bool:
        """
        Returns True if the given Future matches a task that is currently waiting in the pool queue.
        """
        if not isinstance(f, Future):
            raise TypeError(f"Expected Future, got '{type(f).__name__}'")
        with self.__lock:
            return f in (fut for fut, func, args, kwargs in self.__pending)
    
    def apply_async(self, func : Callable[P, R], *args : P.args, **kwargs : P.kwargs):
        """
        Starts the execution of the function func with given arguments in the first available worker.
        Returns Task object to control the execution of the task.
        """
        from .thread.future import Future
        with self.__lock:
            t : "Future[R]" = Future()
            self.__pending.append((t, func, args, kwargs))
        self.__notify()
        return t
        
    def apply(self, func : Callable[P, R], *args : P.args, **kwargs : P.kwargs) -> R:
        """
        Starts the execution of the function func with given arguments in the first available worker and returns the result.
        """
        return self.apply_async(func, *args, **kwargs).result()

    def map_async(self, func : Callable[[*tuple[T]], R], *iterables : Iterable[T], cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> MapIterator[R]:
        """
        Parallel asynchronous version of map. The returned iterator will yield the awaitable results computed by the Pool.
        Note that results from the iterator will be computed in advance.
        "cachesize" limits the memory size of stored results.
        "cachelen" limits the number of results that should be stored.
        """
        from typing import Iterable
        if not callable(func):
            raise TypeError(f"Expected callable, got '{type(func).__name__}'")
        for it in iterables:
            if not isinstance(it, Iterable):
                raise TypeError(f"Expected callable and iterables, got a '{type(it).__name__}'")
        if not isinstance(cachesize, int) and not (isinstance(cachesize, float) and cachesize == float("inf")):
            raise TypeError(f"Expected int or float(\"inf\") for cachesize, got '{type(cachesize).__name__}'")
        if cachesize <= 0:
            raise ValueError(f"Expected positive nonzero integer for cachesize, got {cachesize}")
        if not isinstance(cachelen, int) and not (isinstance(cachelen, float) and cachelen == float("inf")):
            raise TypeError(f"Expected int or float(\"inf\") for cachelen, got '{type(cachelen).__name__}'")
        if cachelen <= 0:
            raise ValueError(f"Expected positive nonzero integer for cachelen, got {cachelen}")
        return self.MapIterator(self, func, zip(*iterables), cachesize if not isinstance(cachesize, float) else None, cachelen if not isinstance(cachelen, float) else None)
        
    def map(self, func : Callable[[*tuple[T]], R], *iterables : Iterable[T], cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
        """
        Parallel version of map. The returned iterator will yield the results computed by the Pool.
        Note that results from the iterator will be computed in advance.
        "cachesize" limits the memory size of stored results.
        "cachelen" limits the number of results that should be stored.
        """
        return (r.result() for r in self.map_async(func, *iterables, cachesize=cachesize, cachelen=cachelen))





module_ready.set()
pool_manager_ready.wait()
del module_ready, pool_manager_ready

del ABCMeta, abstractmethod, deque, RLock, Lock, Event, Callable, Generator, Generic, Iterable, Iterator, ParamSpec, Protocol, TypeVar, WeakSet, ref, P, R, T, Y, W