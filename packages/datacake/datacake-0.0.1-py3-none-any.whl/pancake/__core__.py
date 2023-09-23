from pancake.tools.wrappers import mapping
from json import dumps, loads
from typing import Any, Iterable
from os.path import exists
from os import mkdir

__all__: tuple = (
  "codes", "encode", "gather",
  "match", "reduce", "flatten",
  "scatter", "spatter", "strain",
  "extract", "relabel", "applyto",
  "groupby", "get", "save"
)

codes: set[str] = {
  "$eq", "$ne",
  "$lt", "$le",
  "$gt", "$ge",
  "$in", "$ni",
  "$or",
  "$wi", "$wo",
  "$range", "$source",
  "$start", "$end"
}

@mapping(__data=[])
def get(
  path: str, *,
  __data: list,
  **kwargs
) -> None:
  ...
  with open(
    path, "r",
    encoding="utf-8"
  ) as file:
    ...
    data: list | dict = (
      loads(
        file.read()
      )
    )
  
  data = (
    data["data"] if (
      type(data) is dict
      and "data" in data
    ) else data
  )
    
  __data += (
    data if (
      type(data) is list
    ) else [data]
  )

def save(
  data: list, *,
  path: str,
  **kwargs
) -> None:
  """
  """
  ...
  data = (
    [data] if (
      type(data) is dict
    ) else data
  )
  
  outdir: str = (
    "/".join(
      path.split(
        "/"
      )[:-1]
    )
  )
  
  mkdir(outdir) if (
    not exists(outdir)
  ) else ...
  
  with open(
    path, "w",
    encoding="utf-8"
  ) as file:
    ...
    file.write(
      dumps(
        encode(data),
        indent=2
      )
    )

@mapping(__data=[])
def encode(
  data: dict, *,
  __data: list,
  **kwargs
) -> None:
  ...
  @mapping(__data={})
  def _encode(
    key: int | str, *,
    data: dict,
    __data: dict,
    **kwargs
  ) -> None:
    ...
    __data |= {
      str(key): (
        _encode(
          list(data[key]),
          data=data[key]
        ) if (
          type(
            data[key]
          ) == dict
        ) else encode(
          data[key]
        ) if (
          type(
            data[key]
          ) == list
        ) else data[key]
      )
    }
  
  __data += [
    encode(
      data
    ) if (
      type(
        data
      ) == list
    ) else _encode(
      list(data),
      data=data
    ) if (
      type(
        data
      ) == dict
    ) else data
  ]

def gather(
  pattern: dict, *,
  __pk: tuple=()
) -> dict:
  ...
  pats: dict = {}
  
  for key in pattern:
    ...
    nk: tuple = (
      *__pk, key
    )

    sk: str = (
      ".".join(nk)
    )

    stop: bool = (
      type(
        pattern[key]
      ) != dict
    ) or (
      set(
        pattern[key]
      ) <= codes
    )

    pats |= (
      gather(
        pattern[key],
        __pk=nk
      ) if (
        not stop
      ) else {
        sk: pattern[key]
      }
    )
      
  return pats

@mapping(__matched=True)
def match(
  code: str, *,
  pattern: dict,
  actual: Any,
  __matched: bool,
  **kwargs
) -> bool:
  ...
  # (p, v): tuple = (
  #   pattern.popitem()
  # )
  
  # mat: bool = (
  #   __match(
  #     pattern,
  #     actual
  #   ) if len(
  #     pattern
  #   ) > 0
  #   else True
  # )
  
  expected: Any = (
    pattern[code]
  )
  
  __matched = {
    "$eq": lambda:(
      actual == expected
      and __matched
    ),
    "$ne": lambda:(
      actual != expected
      and __matched
    ),
    "$lt": lambda:(
      actual < expected
      and __matched
    ),
    "$le": lambda:(
      actual <= expected
      and __matched
    ),
    "$gt": lambda:(
      actual > expected
      and __matched
    ),
    "$ge": lambda:(
      actual >= expected
      and __matched
    ),
    "$in": lambda:(
      actual in expected
      and __matched
    ),
    "$ni": lambda:(
      actual not in expected
      and __matched
    ),
    "$or": lambda:(
      match(
        list(expected),
        pattern=expected,
        actual=actual
      ) or __matched
    )
  }[code]()
  
  # pattern |= {p: v}
  
  # return mat

@mapping(__items=[])
def reduce(
  item: Iterable, *,
  __items: Iterable,
  **kwargs
) -> Iterable:
  ...
  t: type = (
    type(
      __items
    )
  )
  
  item = (
    item
  ) if (
    isinstance(
      item,
      Iterable
    ) and type(
      item
    ) != str
  ) else [
    item
  ]

  __items = (
    __items
    + t(item)
  ) if (
    t in (
      list,
      tuple
    )
  ) else (
    __items
    | t(item)
  )

@mapping(__data=[])
def flatten(
  data: dict, *,
  __data: list,
  **kwargs
) -> None:
  ...
  def _flatten(
    data: dict, *,
    __ikey: tuple[int]=(),
    __skey: tuple[str]=()
  ) -> dict:
    ...
    @mapping(dict={})
    def __flatten(
      key: Any, *,
      data: dict,
      __ikey: tuple[int],
      __skey: tuple[str],
      dic: dict
    ) -> None:
      ...
      if type(
        data[key]
      ) not in (list, dict):
        ...
        if type(key) is str:
          ...
          k: tuple = (
            *__ikey,
            None
          )
          
          dic |= {
            k: {}
          } if (
            k not in dic
          ) else {}

          key: str = (
            ".".join((
              *__skey,
              key
            ))
          )

          dic[k] |= {
            key: data[key]
          }
        
        else:
          ...
          k: tuple = (
            *__ikey,
            key
          )
          
          dic |= {
            k: {}
          } if (
            k not in dic
          ) else {}
          
          key: str = (
            ".".join(
              __skey
            )
          )
          
          dic[k] |= {
            key: data[key]
          }
        
      elif type(key) is str:
        ...
        __ikey += (None,)
        __skey += (key,)
        
        dic |= (
          _flatten(
            data[key],
            __ikey=__ikey,
            __skey=__skey
          )
        )
      
      else:
        ...
        __ikey += (key,)
        
        dic |= (
          _flatten(
            data[key],
            __ikey=__ikey,
            __skey=__skey
          )
        )
    
    data = (
      dict(
        enumerate(
          data
        )
      ) if (
        type(
          data
        ) is list
      ) else data
    )
    
    if (
      type(
        data
      ) is not dict
    ): return {}
    
    keys: list = (
      list(data)
    )
    
    __result: dict = (
      __flatten(
        keys,
        data=data,
        __ikey=__ikey,
        __skey=__skey
      )
    )
    
    return __result

  __result: dict = (
    _flatten(
      data
    )
  )
  
  __data += (
    [__result] if (
      len(__result) > 0
    ) else []
  )

@mapping(container=[])
def scatter(
  data: dict, *,
  container: list
) -> None:
  ...
  @mapping(dic=data)
  def _scatter(
    key: str, *,
    dic: dict
  ) -> None:
    ...
    scats: dict = {}
    junk: bool = False
    
    for k in dic:
      ...
      junk = junk or (
        len(key) < len(k)
        and key == k[:len(key)]
      )
      
      scats |= (
        {k: {}} if (
          k not in scats
          and junk
        ) else {}
      )
        
      scats[k] |= (
        dic[key]
        if junk
        else {}
      )
    
    if (
      key in scats
      and junk
    ): scats.pop(key)
      
    if (
      key in dic
      and junk
    ): dic.pop(key)
    
    dic |= {
      k: scats[k]
      for k in scats
    }
      
  keys: list = (
    list(data)
  )
  
  __result: dict = (
    _scatter(
      keys
    )
  )
    
  container += [
    [*__result.values()]
  ]

@mapping(__data=[])
def spatter( # Populates missing keys in mapped data with None
  data: dict, *, # Mapped data from Iterable
  __data: list, # Shared data container
  **kwargs # Allow extra kwargs but don't use
) -> None: # Returns shared data
  """
  Spatter Function:
  Populates missing keys in mapped data with None
  
  Args:
      data (dict): Mapped data from Iterable
      __data (list): Shared data container
      **kwargs: Allow extra kwargs but don't use
  
  Returns:
      None: Returns shared data
  """
  ...
  @mapping(__data=data)
  def _spatter(
    key: str, *,
    __data: dict
  ) -> None:
    ...
    __data = (
      __data | {
        key: None
      } if (
        key not in __data
      ) else __data
    )
    
  __data += [
    _spatter(
      list(
        data
      )
    )
  ]

@mapping(container=[])
def strain(
  data: dict, *,
  conditions: list,
  container: list
) -> None:
  ...
  @mapping(dic={})
  def _strain(
    condition: dict, *,
    data: dict,
    dic: dict
  ) -> None:
    ...
    cons: dict = (
      gather(
        condition
      )
    )
    # TODO: Move this to __match
    for key in cons:
      ...
      matched: bool = (
        key in data
        and match(
          list(cons[key]),
          pattern=cons[key],
          actual=data[key]
        )
      )

      if (
        not matched
      ): return
    
    dic = data

  __result: dict = (
    _strain(
      conditions,
      data=data
    )
  )
  
  container += (
    [__result] if (
      len(__result) > 0
    ) else []
  )
  
@mapping(container=[])
def extract(
  data: dict, *,
  extractions: list,
  container: list
) -> None:
  ...
  @mapping(dic=data)
  def _extract(
    extraction: dict, *,
    dic: dict
  ) -> None:
    ...
    exts: dict = (
      gather(
        extraction
      )
    )
    
    keys: list = (
      list(exts)
    )
    
    vals: list = (
      list(
        exts.values()
      )
    )
    
    if {"$range", "$source"} < set(vals):
      ...
      key: str = keys[
        vals.index("$range")
      ]
      
      source: str = dic[keys[
        vals.index("$source")
      ]]
      
      start: int = (
        dic[keys[
          vals.index("$start")
        ]] if "$start" in vals
        else None
      )
      
      end: int = (
        dic[keys[
          vals.index("$end")
        ]] if "$end" in vals
        else None
      )
      
      dic[key] = (
        source[start:end]
        if None not in (start, end)
        else source[start:]
        if start is not None
        else source[:end]
        if end is not None
        else None
      )
  
  __result: dict = (
    _extract(
      extractions
    )
  )
  
  container += [
    __result
  ]

# @mapping(container=[])
# def __relabel(
#   data: dict, *,
#   attributes: list,
#   container: list
# ) -> None:
  # ...
  # @mapping(dic={})
  # def _relabel(
  #   attribute: dict, *,
  #   data: dict,
  #   dic: dict
  # ) -> None:
  #   ...
  #   atts: dict = (
  #     __gather(
  #       attribute
  #     )
  #   )
    
  #   tmp: dict = {}
      
  #   for key in atts:
  #     ...
  #     skip: bool = (
  #       key not in data
  #       or data[key] == None
  #     )
      
  #     if skip: return None
      
  #     tmp |= {
  #       atts[key]: data[key]
  #     }
      
  #   dic = tmp
  
  # __result: dict = (
  #   _relabel(
  #     attributes,
  #     data=data
  #   )
  # )
  
  # container += (
  #   [__result]
  #   if len(__result) > 0
  #   else []
  # )
  
@mapping(container={})
def relabel(*,
  data: dict,
  atts: dict,
  container: dict,
  **kwargs
) -> None:
  """
  Return
  """
  ...
  atts = (
    gather(
      atts
    )
  )
    
  tmp: dict = {}
    
  for key in atts:
    ...
    skip: bool = (
      key not in data
      or data[key] == None
    )
    
    if skip: return
    
    tmp |= {
      atts[key]: data[key]
    }
    
  container = tmp

@mapping(container=[])
def applyto(
  data: dict, *,
  applications: list,
  container: list
) -> None:
  ...
  #TODO: Create some common use functions and code strings
  # Create custom code string detection and parsing
  @mapping(dic=data)
  def _applyto(
    application: dict, *,
    dic: dict
  ) -> None:
    ...
    apps: dict = (
      gather(
        application
      )
    )
    
    dic |= (
      {
        key: apps[key](
          dic[key]
        )
      }
      if key in dic
      else {}
      for key in apps
    )
  
  __result: dict = (
    _applyto(
      applications
    )
  )
  
  container += [
    __result
  ]

@mapping(container={})
def groupby(
  key: str, *,
  data: list,
  container: dict
) -> None:
  ...
  @mapping(dic={})
  def _groupby(
    data: dict, *,
    key: str,
    dic: list
  ) -> None:
    ...
    if key in data:
      ...
      dic |= (
        {
          data[key]:
          {key: data[key]}
        }
        if data[key] not in dic
        else {}
      )
        
      for k in data:
        ...
        if k != key:
          ...
          dic[data[key]] |= (
            {k: []}
            if k not in dic[data[key]]
            else {}
          )
          
          dic[data[key]][k] += [data[k]]
    
  __result: dict = (
    _groupby(
      data,
      key
    )
  )
  
  container |= {
    key: [
      *__result.values()
    ]
  }

  # asserts: dict = {
  #   a: False
  #   for a in __all__[1:]
  # }
  
  # tests: dict = {
    
  # }

# def __map(*iterables, func, **kwargs):
#   ...
#   if len(kwargs) > 0:
#     ...
#     func = partial(func, **kwargs)
    
#   return map(func, *iterables)

# def __reduce(iterable, initial=object(), *, func, **kwargs):
#   ...
#   if len(kwargs) > 0:
#     ...
#     func = partial(func, **kwargs)
    
#   return reduce(func, iterable, initial)

# def __strat(
#   data: list[dict] | dict
# ) -> list[dict] | dict:
#   ...
#   if type(data) is list:
#     ...
#     return list(
#       map(
#         __strat,
#         data
#       )
#     )
  
#   elif type(data) is dict:
#     ...
#     strats: dict = {}
    
#     for key in data:
#       ...
#       if type(data[key]) not in (dict, list):
#         ...
#         strats |= {
#           str(key): data[key]
#         }
      
#       else:
#         ...
#         strats |= {
#           str(key): __strat(data[key])
#         }
      
#     return strats
  
#   else:
#     ...
#     return data
    
# def __gat(
#   pattern: dict,
#   pk: tuple=()
# ) -> dict:
#   ...
#   pats: dict = {}
  
#   for key in pattern:
#     ...
#     if (
#       type(pattern[key]) is not dict
#       or type(pattern[key]) is Callable
#       or set(pattern[key]) <= codes
#     ):
#       ...
#       pats |= {
#         ".".join(pk + (key,)): pattern[key]
#       }
    
#     else:
#       ...
#       pats |= __gat(
#         pattern[key],
#         pk + (key,)
#       )
      
#   return pats

# def simmer(items, initial=None):
#   ...
#   def __simmer(
#     items: set | list | tuple,
#     *,
#     shared: dict
#   ) -> set | list | tuple:
#     ...
#     # Do not reduce dictionaries, raise TypeError
#     if type(shared["result"]) not in (set, list, tuple):
#       ...
#       message: str = (
#         f"Cannot reduce to {type(initial)}"
#         f" type, only [set, list, tuple] allowed"
#       )
      
#       raise TypeError(message)
    
#     # Get 
#     t: type = type(items)
    
#     if (
#       type(items) is str
#       or not isinstance(items, Iterable)
#     ):
#       ...
#       items = [items]

#     shared["result"] = (
#       shared["result"] + t(items)
#       if type(shared["result"]) in (list, tuple)
#       else shared["result"] | t(items)
#     )

# def __flatten(
#   data: list[dict] | dict,
#   *,
#   __ikey: tuple[int]=(),
#   __skey: tuple[str]=()
# ) -> dict:
#   ...
#   if type(data) is list:
#     ...
#     data = dict(enumerate(data))
  
#   elif type(data) is not dict:
#     ...
#     return {}
  
#   flats: dict = {}
  
#   for key in data:
#     ...
#     if type(data[key]) not in (list, dict):
#       ...
#       if type(key) is str:
#         ...
#         k: tuple = __ikey + (None,)
        
#         if k not in flats:
#           ...
#           flats |= {k: {}}

#         flats[k] |= {
#           ".".join(__skey + (key,)): data[key]
#         }
      
#       else:
#         ...
#         k: tuple = __ikey + (key,)
        
#         if k not in flats:
#           ...
#           flats |= {k: {}}
        
#         flats[k] |= {
#           ".".join(__skey): data[key]
#         }
        
#     elif type(key) is str:
#       ...
#       flats |= __flatten(
#         data[key],
#         __ikey=__ikey + (None,),
#         __skey=__skey + (key,)
#       )
    
#     else:
#       ...
#       flats |= __flatten(
#         data[key],
#         __ikey=__ikey + (key,),
#         __skey=__skey
#       )
    
#   return flats

# def __scatter(
#   data: dict
# ) -> dict:
#   ...
#   if type(data) is not dict:
#     ...
#     return {}
  
#   scats: dict = {}
#   junks: list = []
  
#   for key in data:
#     ...
#     for k in data:
#       ...
#       if (
#         len(key) < len(k)
#         and key == k[:len(key)]
#       ):
#         ...
#         if key not in junks:
#           ...
#           junks += [key]
        
#         if k not in scats:
#           ...
#           scats |= {k: {}}
          
#         scats[k] |= data[key]
  
#   for key in junks:
#     ...
#     if key in scats:
#       ...
#       scats.pop(key)
    
#     if key in data:
#       ...
#       data.pop(key)
      
#   for key in scats:
#     ...
#     data[key] |= scats[key]
  
#   return list(data.values())

# def __spatter(
#   data: dict,
#   keys: set[str]
# ) -> dict:
#   ...
#   for key in keys:
#     ...
#     if key not in data:
#       ...
#       data |= {key: None}

#   return data

# def __strain(
#   data: dict,
#   conditions: list[dict] | dict
# ) -> dict:
#   ...
#   if type(conditions) is dict:
#     ...
#     conditions = [conditions]
    
#   keep: bool = False
  
#   for condition in conditions:
#     ...
#     cons: dict = __gat(condition)
    
#     for key in cons:
#       ...
#       if (
#         key in data
#         and __mat(
#           cons[key],
#           data[key]
#         )
#       ):
#         ...
#         keep = True
        
#   if not keep:
#     ...
#     return {}
  
#   return data

# def __extract(
#   data: dict,
#   extractions: list[dict] | dict
# ) -> dict:
#   ...
#   if type(extractions) is dict:
#     ...
#     extractions = [extractions]
    
#   for extraction in extractions:
#     ...
#     exts: dict = __gat(extraction)
#     keys: list = list(exts.keys())
#     vals: list = list(exts.values())
    
#     if {"$range", "$source"} < set(vals):
#       ...
#       key: str = keys[vals.index("$range")]
      
#       source: str = data[keys[vals.index("$source")]]
      
#       start: int = (
#         data[keys[vals.index("$start")]]
#         if "$start" in vals
#         else None
#       )
      
#       end: int = (
#         data[keys[vals.index("$end")]]
#         if "$end" in vals
#         else None
#       )
      
#       data[key] = (
#         source[start:end]
#         if None not in (start, end)
#         else source[start:]
#         if start is not None
#         else source[:end]
#         if end is not None
#         else None
#       )
      
#   return data

# def __relabel(
#   data: dict,
#   attributes: list[dict] | dict
# ) -> list[dict]:
#   ...
#   if type(attributes) is dict:
#     ...
#     attributes = [attributes]
    
#   d: dict = {}
    
#   for attribute in attributes:
#     ...
#     atts: dict = __gat(
#       attribute
#     )
      
#     for key in atts:
#       ...
#       if (
#         key in data
#         and data[key] == None
#       ):
#         ...
#         return {}
      
#       d |= {atts[key]: data[key]}
      
#   return d

# def __applyto(
#   data: dict,
#   applications: list[dict] | dict
# ) -> list[dict]:
#   ...
#   if type(applications) is dict:
#     ...
#     applications = [applications]
    
#   for application in applications:
#     ...
#     #TODO: Create some common use functions and code strings
#     # Create custom code string detection and parsing
#     apps: dict = __gat(
#       application
#     )
    
#     for key in apps:
#       ...
#       if key in data:
#         ...
#         data[key] = apps[key](
#           data[key]
#         )
        
#   return data

# def __groupby(
#   data: list[dict],
#   key: str
# ) -> list[dict]:
#   ...
#   # def __entry()
  
  
#   groups: dict = {}
  
#   for dat in data:
#     ...
#     if key in dat:
#       ...
#       if dat[key] not in groups:
#         ...
#         groups |= {
#           dat[key]: {
#             key: dat[key]
#           }
#         }
        
#       for k in dat:
#         ...
#         if k != key:
#           ...
#           if k not in groups[dat[key]]:
#             ...
#             groups[dat[key]] |= {k: []}
          
#           groups[dat[key]][k] += [dat[k]]
          
#   return list(
#     groups.values()
#   )

# def __batch(
#   data: dict,
#   conditions: list[dict] | dict=None,
#   extractions: list[dict] | dict=None,
#   applications: list[dict] | dict=None,
#   attributes: list[dict] | dict=None
# ) -> dict:
#   ...
#   with (
#     ThreadPoolExecutor() as pool,
#     Binding(__strain, data) as __stn,
#     Binding(__extract, data) as __ext,
#     Binding(__applyto, data) as __app,
#     Binding(__relabel, data) as __lbl,
#   ):
#     ...
#     pool.map(
#       __stn,
#       conditions
#     ) if conditions else data
    
#     pool.map(
#       __ext,
#       extractions
#     ) if extractions else data
      
#     pool.map(
#       __app,
#       applications
#     ) if applications else data

#     pool.map(
#       __lbl,
#       attributes
#     ) if attributes else data
    
#   return data
  
  