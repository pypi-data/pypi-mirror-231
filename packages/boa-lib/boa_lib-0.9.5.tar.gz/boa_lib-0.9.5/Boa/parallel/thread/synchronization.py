"""
This module adds some useful tools for synchronization accros a multithreaded system.
"""

from types import TracebackType
from typing import Callable, ParamSpec, TypeVar
from threading import Thread

__all__ = ["PLock", "ExclusionGroup", "exclusive", "critical"]





class PLock:

    """
    An Passable Recursive Lock class with a few more functionnalities which allow to transfer the lock to another thread with priority.
    """

    from threading import Lock as __Lock, Thread as __Thread, current_thread as __current_thread
    __current_thread = staticmethod(__current_thread)
    from time import time_ns as __time_ns

    __slots__ = {
        "__lock" : "The base lock used to acquire the RLock",
        "__level" : "The recursion level of the RLock",
        "__owner_thread" : "The thread that currently holds the lock",
        "__pass_lock" : "The lock used to synchronize the passing of the lock to the priority thread",
        "__next_thread" : "A thread that should acquire the lock next with highest priority"
    }

    def __init__(self) -> None:
        self.__lock = self.__Lock()
        self.__level : int = 0
        self.__owner_thread : "Thread | None" = None
        self.__pass_lock = self.__Lock()
        self.__next_thread : "Thread | None" = None
    
    def __repr__(self):
        """
        Implements repr(self).
        """
        s = f"<{type(self).__name__} object at {hex(id(self))}"
        if (t := self.__owner_thread) != None:
            s += f" owned by {t}>"
        else:
            s += " unlocked>"
        return s

    def __enter__(self):
        """
        Implements with self.
        """
        self.acquire()
    
    def __exit__(self, exc_type : type[BaseException], exc : BaseException, traceback : TracebackType):
        """
        Implements with self.
        """
        self.release()
    
    def acquire(self, blocking : bool = True, timeout : float = float("inf")) -> bool:
        """
        Acquires the lock.
        blocking specify if the operation should block until the lock has been acquired or until the optional timeout has been reached.
        Returns True if the lock is held on return, False otherwise.
        """
        if not isinstance(blocking, bool):
            raise TypeError(f"Expected bool, got '{type(blocking).__name__}'")
        try:
            timeout = float(timeout)
        except:
            pass
        if not isinstance(timeout, float):
            raise TypeError(f"Expected float for timeout, got '{type(timeout).__name__}'")
        if timeout < 0:
            raise ValueError(f"Expected positive value for timeout, got {timeout}")
        if self.__owner_thread == self.__current_thread():
            self.__level += 1
            return True
        if timeout == 0:
            blocking = False
        if timeout == float("inf"):
            timeout = -1
        timeout_0 = timeout
        t0 = self.__time_ns()
        while True:
            if not self.__lock.acquire(blocking, timeout):
                return False
            
            timeout = max(timeout_0 - (self.__time_ns() - t0) / 1000000000, -1)
            if timeout < 0 and timeout != -1:
                return False

            next_thread = self.__next_thread
            if next_thread != None and not next_thread.is_alive():  # The prioritized thread has died. Forget about priority.
                next_thread, self.__next_thread = None, None
                self.__pass_lock.release()

            if self.__pass_lock.acquire(False) or next_thread == self.__current_thread():
                if next_thread != None:      # The calling thread received the lock by priority
                    self.__next_thread = None
                self.__pass_lock.release()
                self.__owner_thread = self.__current_thread()
                self.__level = 1
                return True
            
            else:
                self.__lock.release()

            timeout = max(timeout_0 - (self.__time_ns() - t0) / 1000000000, -1)
            if timeout < 0 and timeout != -1:
                return False

    def release(self):
        """
        Lowers the ownership level by one. If it reaches zero, releases the lock so other threads can try acquiering it.
        """
        if self.__owner_thread != self.__current_thread():
            raise RuntimeError("Trying to release un-acquired lock")
        self.__level -= 1
        if self.__level == 0:
            self.__owner_thread = None
            self.__lock.release()

    @property
    def acquired(self) -> bool:
        """
        Returns True if the lock is currently owned by the calling thread.
        """
        return self.__owner_thread == self.__current_thread()

    def pass_on(self, next_thread : Thread):
        """
        Ensures that the next thread to acquire the lock is the one given as argument.
        Make sure that this thread will try to acquire it afterwards, to avoid causing a deadlock.
        """
        if not isinstance(next_thread, self.__Thread):
            raise TypeError(f"Expected Thread, got '{type(next_thread).__name__}'")
        if not self.acquired:
            raise RuntimeError("Cannot pass the lock without acquiering it first")
        self.__pass_lock.acquire()
        self.__next_thread = next_thread





P = ParamSpec("P")
T = TypeVar("T")

class ExclusionGroup:

    """
    This is used to create a mutual exclusion group.
    It is like using a RLock but that can be used as a decorator to make a function mutually exclusive in regards to anyone using this same function.
    """

    def __init__(self) -> None:
        from threading import RLock
        self.__lock = RLock()

    def __call__(self, f : Callable[P, T]) -> Callable[P, T]:
        from Viper.meta.utils import signature_def, signature_call
        from functools import wraps

        sig = "@wraps(old_target)\n"

        sig_def, env = signature_def(f, init_env = {"old_target" : f, "wraps" : wraps, "__lock" : self})
        
        code = sig + sig_def
        
        code += "\n\twith __lock:\n\t\t"

        code += "return old_target("

        sig_call = signature_call(f, decorate = False)

        code += sig_call + ")"

        exec(code, env)

        return env[f.__name__]
    
    def acquire(self, blocking : bool = True, timeout : float = -1):
        """
        Acquires the exclusion group. Works exactly like RLock.acquire().
        """
        return self.__lock.acquire(blocking, timeout)
    
    def release(self):
        """
        Releases the exclusion group. Works exactly like RLock.release().
        """
        self.__lock.release()
    
    def __enter__(self):
        self.__lock.acquire()

    def __exit__(self, exc_type, exc_value, traceback):
        self.__lock.release()





def exclusive(f : Callable[P, T]) -> Callable[P, T]:

    return ExclusionGroup()(f)
    
critical = exclusive





del Callable, ParamSpec, TypeVar, Thread, TracebackType, P, T