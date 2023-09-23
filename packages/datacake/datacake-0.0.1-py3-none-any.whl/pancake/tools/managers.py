from types import TracebackType
from typing import (
  Callable, ContextManager,
  overload, Type,
)
from pancake.types.binding import *
from pancake.types.mapping import *
from pancake.types.generic import *
from pancake.tools.wrappers import (
  mapping, binding
)

__all__: tuple = (
  "Mapping", "Binding", "Singleton"
)

class Mapping(ContextManager):
  ...
  __mapped: Mapped
  
  def __init__(
    self,
    method: MapMethod,
    **inits: MapInits
  ) -> None:
    ...
    self.__mapped = mapping(
      method,
      **inits
    )
    
  def __call__(
    self,
    *items: MapItems,
    **inits: MapInits
  ) -> MapReturn:
    ...
    __result: MapReturn = (
      self.__mapped(
        *items,
        **inits
      )
    )
      
    return __result
      
  def __enter__(
    self
  ) -> "Mapping":
    ...
    return self
    
  def __exit__(
    self,
    exc: type[BaseException] | None,
    val: BaseException | None,
    trc: TracebackType | None
  ) -> bool | None:
    ...
 
class Binding(ContextManager):
  ...
  __bound: Bound
  
  def __init__(
    self,
    *items: BindItems,
    **inits: BindInits
  ) -> None:
    ...
    self.__bound = binding(
      *items,
      **inits
    )
    
  def __call__(
    self,
    *items: BindItems,
    **inits: BindInits
  ) -> ReturnType | "Binding":
    ...
    __result = (
      self.__bound(
        *items,
        **inits
      )
    )
    
    (
      __result,
      self.__bound
    ) = (
      self,
      __result
    ) if callable(
      __result
    ) else (
      __result,
      self.__bound
    )
    
    return __result
  
  def __enter__(
    self
  ) -> "Binding":
    ...
    return self
    
  def __exit__(
    self,
    exc: type[BaseException] | None,
    val: BaseException | None,
    trc: TracebackType | None
  ) -> bool | None:
    ...

class Singleton(ContextManager):
  ...
  __instance: object
  
  def __new__(
    self,
    cls: ClassType
  ) -> "Singleton":
    ...
    self: "Singleton" = super().__new__(self)
    self.__instance = cls()
    
    return self
  
  def __call__(
    self,
    *args: PosArgs,
    **kwds: KwdArgs
  ) -> ReturnType:
    ...
    __result: ReturnType = (
      self.__instance(
        *args,
        **kwds
      )
    )
    
    return __result
  
  def __enter__(
    self
  ) -> "Singleton":
    ...
    return self
  
  def __exit__(
    self,
    exc: type[BaseException] | None,
    val: BaseException | None,
    trc: TracebackType | None
  ) -> bool | None:
    ...
  
  def call(
    self,
    name: str,
    *args: PosArgs,
    **kwds: KwdArgs
  ) -> ReturnType:
    ...
    __method: Callable = (
      getattr(
        self.__instance,
        name
      )
    )
    
    __result: ReturnType = (
      __method(
        *args,
        **kwds
      )
    )
    
    return __result
