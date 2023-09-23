from pancake.types.generic import *
from typing import Callable, Dict, Optional, Tuple, TypeAlias, Union

__all__: tuple = (
  "BindItems",
  "BindInits",
  "BindMethods",
  "Bound", "Binder",
)

BindItems: TypeAlias = PosArgs
BindInits: TypeAlias = KwdArgs

BindMethods: TypeAlias = Tuple[
  MethodType, ...
]

Bound: TypeAlias = Callable[
  [BindItems, BindInits],
  ReturnType
]

Binder: TypeAlias = Callable[
  [BindMethods, BindInits],
  Bound
]