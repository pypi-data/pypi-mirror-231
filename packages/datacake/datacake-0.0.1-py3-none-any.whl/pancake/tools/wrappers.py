
from pancake.types.generic import *
from pancake.types.mapping import *
from pancake.types.binding import *
from pancake.tools.managers import Singleton
from time import perf_counter
from typing import Callable, NamedTuple
from functools import partial, reduce, wraps

__all__: tuple = (
  "mapping", "binding",
  "singleton", "timing"
)

# def mapping(
#   method: MapMethod=None,
#   __initials: MapInits={},
#   **initials: MapInits
# ) -> Mapper | Mapped:
#   ...
#   @wraps(method)
#   def _mapping(
#     *items: MapArgs,
#     __items: MapArgs=(),
#     __initials: MapInits={},
#     **initials: MapInits
#   ) -> MapReturn:
#     ...
#     __items += items
#     __initials |= initials

#     if (len(items), len(initials)) != (0, 0):
#       ...
#       __mapping = partial(
#         _mapping,
#         __items=__items,
#         __initials=__initials
#       )
      
#       return __mapping
    
#     if len(__items) == 0:
#       ...
#       message: str = (
#         f"Invalid attempt to map"
#         f" <function {method.__name__}>"
#         f" without <MapItems>"
#       )
      
#       raise Exception(message)
    
#     if len(__initials) == 0:
#       ...
#       message: str = (
#         f"Atleast one <MapInit> required"
#       )
      
#       raise Exception(message)
    
#     __mapping = partial(
#       method,
#       **__initials
#     )
    
#     __result = tuple(map(
#       __mapping,
#       *__items
#     ))
    
#     return __initials or __result
  
#   __initials |= initials
  
#   __mapping = partial(
#     (
#       _mapping
#       if method
#       else mapping
#     ),
#     __initials=__initials
#   )
  
#   return __mapping

def mapping(
  method: MapMethod=None,
  **inits: MapInits
) -> Mapper | Mapped:
  ...
  def _mapping(
    _method: MapMethod
  ) -> Mapped:
    ...
    @wraps(_method)
    def __mapping(
      *__items: MapItems,
      **__inits: MapInits
    ) -> MapReturn:
      ...
      __inits |= inits
      
      __mapped = map(
        partial(
          _method,
          **__inits
        ), *__items
      )
      
      return tuple(
        __mapped
      ) and __inits
      
    return __mapping
  
  return (
    _mapping
    if method is None
    else _mapping(method)
  )
  
# def __reduce(iterable, initial=object(), *, func, **kwargs):
#   ...
#   if len(kwargs) > 0:
#     ...
#     func = partial(func, **kwargs)
    
#   return reduce(func, iterable, initial)

# def reduction(
#   method: ReduceMethod=None,
#   **initials: ReduceInits
# ) -> Reducer | Reduced:
#   ...
#   def _reduction(
#     method: ReduceMethod
#   ) -> Reduced:
#     ...
#     @wraps(method)
#     def __reduction(
#       *items: ReduceArgs,
#       **inits: ReduceInits
#     ) -> ReduceReturn:
#       ...
#       inits |= initials
      
#       __reduced = partial(
#         method,
#         **inits
#       )
      
#       __result: ReduceReturn = (
#         tuple(reduce(
#           __reduced,
#           *items
#         )) and inits
#       )
      
#       return __result
  
#     return __reduction
  
#   return (
#     _reduction
#     if method is None
#     else _reduction(method)
#   )

# def binding(
#   *methods: BindMethods,
#   **kwargs: BindKeyArgs
# ) -> Bound:
#   ...
#   def _binding(
#     *args: BindArgs,
#     __args: BindArgs=(),
#     __methods: BindMethods=(),
#     __kwargs: BindKeyArgs={},
#     **kwargs: BindKeyArgs
#   ) -> ReturnType:
#     ...
#     methods = tuple((
#       arg
#       for arg in args
#       if isinstance(arg, BindMethod)
#     ))
    
#     args = tuple((
#       arg
#       for arg in args
#       if not isinstance(arg, Callable)
#     ))
    
#     __methods += methods
#     __args += args
#     __kwargs |= kwargs
    
#     if len(methods) > 0:
#       ...
#       __binding = partial(
#         _binding,
#         __args=__args,
#         __methods=__methods,
#         __kwargs=__kwargs
#       )
      
#       return __binding
    
#     __method: BindMethod = __methods[-1]
#     __methods = __methods[:-1]
    
#     __result: ReturnType = __method(
#       *__args,
#       **__kwargs
#     )
    
#     for __method in __methods:
#       ...
#       __result = __method(__result)
      
#     return __result
  
#   __binding = partial(
#     _binding,
#     __methods=methods,
#     __kwargs=kwargs
#   )
  
#   return __binding

def binding(
  *items: BindItems,
  **inits: BindInits
) -> Bound:
  ...
  def _binding(
    *items: BindItems,
    _items: BindItems,
    _methods: BindMethods,
    _inits: BindInits,
    **inits: BindInits
  ) -> ReturnType:
    ...
    def __binding(*,
      __items: BindItems,
      __method: MethodType,
      __methods: BindMethods,
      __inits: BindInits
    ) -> ReturnType:
      ...
      __result: ReturnType = (
        __method(
          *__items,
          **__inits
        )
      )
      
      return __binding(
        __items=(__result,),
        __method=__methods[-1],
        __methods=__methods[:-1],
        __inits=__inits
      ) if (
        len(__methods)
      ) else __result
      
    (
      _items,
      _method,
      _methods
    ) = (
      _items,
      _methods[-1],
      _methods[:-1]
    ) if (
      not len(items)
    ) else (
      _items, None,
      _methods + items
    ) if (
      all(map(
        callable,
        items
      ))
    ) else (
      _items + (
        arg 
        for arg in items
        if not callable(arg)
      ), (
        arg
        for arg in items
        if callable(arg)
      )[-1], _methods + (
        arg
        for arg in items
        if callable(arg)
      )[:-1]
    ) if (
      any(map(
        callable,
        items
      ))
    ) else (
      _items + items,
      _methods[-1],
      _methods[:-1]
    )
    
    _inits |= inits
    
    return __binding(
      __items=_items,
      __method=_method,
      __methods=_methods,
      __inits=_inits
    ) if (
      _method
    ) else partial(
      _binding,
      _args=_items,
      _methods=_methods,
      _kwargs=_inits
    )
  
  (
    items,
    methods
  ) = (
    (), items
  ) if (
    all(map(
      callable,
      items
    ))
  ) else ((
    arg 
    for arg in items
    if not callable(arg)
  ), (
    arg
    for arg in items
    if callable(arg)
  )) if any(
    map(
      callable,
      items
    )
  ) else (
    items, ()
  )
  
  return partial(
    _binding,
    _args=items,
    _methods=methods,
    _kwargs=inits
  )

# def binding(
#   *methods: BindMethods,
#   **kwargs: BindInits
# ) -> Bound:
#   ...
#   def _binding(
#     method: MethodType,
#     *args: BindItems,
#     **kwds: BindInits
#   ) -> ReturnType:
#     ...
#     def __binding(*,
#       __method: MethodType,
#       __methods: BindMethods,
#       __args: BindItems,
#       __kwds: BindInits
#     ) -> ReturnType:
#       ...
#       __result: ReturnType = (
#         __method(
#           *__args,
#           **__kwds
#         )
#       )
      
      
      
#       for method in reversed(methods[:-1]):
#         ...
#         __result = method(
#           *__result
#         )
        
#       return __result
      
#     return binding(
#       *(*methods, method),
#       **(kwargs | kwds)
#     ) if (
#       isinstance(
#         method, Callable
#       ) and len(args) == 0
#     ) else __binding(
#       __method=methods[-1],
#       __methods=methods[:-1],
#       __args=(method, *args),
#       __kwds=(kwargs | kwds)
#     )
  
#   return _binding

def singleton(
  cls: ClassType
) -> Singleton:
  ...
  return Singleton(cls)

def timing(
  method: Callable
) -> Callable:
  ...
  @wraps(method)
  def _timing(
    *args,
    **kwargs
  ) -> ReturnType:
    ...
    start: float = perf_counter()
    print(f"{method.__name__} ...")
    
    result = method(
      *args,
      **kwargs
    )
    
    end: float = (
      perf_counter()
      - start
    )
    
    mins = int(end / 60)
    secs = int(end % 60)
    
    print(
      f"...",
      f"{'0' if mins < 10 else ''}{mins}m",
      f"{'0' if secs < 10 else ''}{secs}s",
      f"{method.__name__}"
    )
    
    return result
  
  return _timing
