"""
This module adds a few useful class decorators to Python.
"""

from typing import Callable, Concatenate, Generic, Type, TypeVar, ParamSpec

__all__ = ["semistaticmethod", "hybridmethod", "staticproperty"]





R = TypeVar("R")
P = ParamSpec("P")
T = TypeVar("T")

class semistaticmethod(Generic[P, R, T]):

    """
    This decorator makes a function behave like a method when called from a class instance, but when called from the class, the "self" argument will be None.
    """

    def __init__(self, func : Callable[Concatenate[T | None, P], R]) -> None:
        self.__func__ = func
    
    def __get__(self, obj : T | None, cls : Type[T]) -> Callable[P, R]:
        from functools import wraps

        @wraps(self.__func__)
        def semi(*args : P.args, **kwargs : P.kwargs):      # type: ignore
            return self.__func__(obj, *args, **kwargs)      # type: ignore

        semi.__func__ = semi.im_func = self.__func__        # type: ignore
        semi.__self__ = semi.im_self = obj                  # type: ignore

        return semi                                         # type: ignore





class hybridmethod(Generic[P, R, T]):

    """
    This decorator makes a function behave like a method when called from a class instance, and as a classmethod when called from a class.
    """

    def __init__(self, func : Callable[Concatenate[T | Type[T], P], R]) -> None:
        self.__func__ = func
    
    def __get__(self, obj : T | None, cls : Type[T]) -> Callable[P, R]:
        from functools import wraps

        context = obj if obj is not None else cls

        @wraps(self.__func__)
        def hybrid(*args : P.args, **kwargs : P.kwargs):        # type: ignore
            return self.__func__(context, *args, **kwargs)      # type: ignore

        hybrid.__func__ = hybrid.im_func = self.__func__        # type: ignore
        hybrid.__self__ = hybrid.im_self = context              # type: ignore

        return hybrid                                           # type: ignore
    




class staticproperty(property, Generic[P, R, T]):

    """
    This decorator transforms a method into a static property of the class (it takes no self/cls argument).
    You can use setter, getter and deleter to set the different staticproperty descriptors.
    """

    def __init__(self, fget : Callable[[], R] | None = None, fset : Callable[[R], None] | None = None, fdel : Callable[[], None] | None = None, *args) -> None:
        self.__fget : Callable[[], R] | None = None
        self.__fset : Callable[[R], None] | None = None
        self.__fdel : Callable[[], None] | None = None
        # print("Got arguments", (self, fget, fset, fdel) + args)
        if fget != None:
            self.__fget = staticmethod(fget)
        if fset != None:
            self.__fset = staticmethod(fset)
        if fdel != None:
            self.__fdel = staticmethod(fdel)
        self.__name__ : str = ""
        self.__cls__ : type = type

    @property
    def fget(self) -> Callable[[], R] | None:
        """
        The getter function of this staticproperty.
        """
        return self.__fget
    
    @property
    def fset(self) -> Callable[[R], None] | None:
        """
        The setter function of this staticproperty.
        """
        return self.__fset
    
    @property
    def fdel(self) -> Callable[[], None] | None:
        """
        The deleter function of this staticproperty.
        """
        return self.__fdel
    
    def __set_name__(self, cls : Type[T], name : str):
        self.__name__ = name
        self.__cls__ = cls
    
    def __get__(self, obj : T | None, cls : Type[T] | None = None) -> R:
        if not self.__fget:
            raise AttributeError("staticproperty '{}' of '{}' {} has not getter".format(self.__name__, self.__cls__, "object" if obj is not None else "class"))
        try:
            return self.__fget()
        except AttributeError as e:
            raise e from None
    
    def __set__(self, obj : T | None, value : R):
        if not self.__fset:
            raise AttributeError("staticproperty '{}' of '{}' {} has not setter".format(self.__name__, self.__cls__, "object" if obj is not None else "class"))
        try:
            return self.__fset(value)
        except AttributeError as e:
            raise e from None
    
    def __delete__(self, obj : T | None):
        if not self.__fdel:
            raise AttributeError("staticproperty '{}' of '{}' {} has not deleter".format(self.__name__, self.__cls__, "object" if obj is not None else "class"))
        try:
            return self.__fdel()
        except AttributeError as e:
            raise e from None
        
    def getter(self, fget : Callable[[], R]) -> "staticproperty":
        """
        Descriptor to obtain a copy of the staticproperty with a different getter.
        """
        self.__fget = staticmethod(fget)
        return self
    
    def setter(self, fset : Callable[[R], None]) -> "staticproperty":
        """
        Descriptor to obtain a copy of the staticproperty with a different setter.
        """
        self.__fset = staticmethod(fset)
        return self
    
    def deleter(self, fdel : Callable[[], None]) -> "staticproperty":
        """
        Descriptor to obtain a copy of the staticproperty with a different deleter.
        """
        self.__fdel = staticmethod(fdel)
        return self





del Callable, Type, TypeVar, ParamSpec