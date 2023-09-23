from typing import (
  Any, Callable, Set, Tuple, Type,
  TypeAlias, TypeVar
)

__all__: tuple = (
  "ItemType", "ReturnType",
  "PosArgs", "KwdArgs",
  "ClassType", "MethodType"
)

ItemType = TypeVar("ItemType")
ReturnType = TypeVar("ReturnType")

PosArgs = TypeVar("PosArgs", bound=Tuple)
KwdArgs = TypeVar("KwdArgs", bound=Set[Tuple])

ClassType = TypeVar("ClassType", bound=Type[Type])
MethodType: TypeAlias = Callable[
  [PosArgs, KwdArgs],
  ReturnType
]