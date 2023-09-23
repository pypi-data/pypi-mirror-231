from pancake.types.generic import *
from typing import (
  Callable, Iterable, Tuple,
  TypeAlias, Union, Set
)

__all__: tuple = (
  "MapItems", "MapInits",
  "Mapper", "Mapped",
  "MapMethod","MapReturn",
)

MapItems: TypeAlias = PosArgs
MapInits: TypeAlias = KwdArgs

MapReturn: TypeAlias = Union[
  ReturnType, Iterable[ReturnType]
]

MapMethod: TypeAlias = MethodType

Mapped: TypeAlias = Callable[
  [MapItems, MapInits],
  MapReturn
]

Mapper: TypeAlias = Callable[
  [MapMethod],
  Mapped
]
