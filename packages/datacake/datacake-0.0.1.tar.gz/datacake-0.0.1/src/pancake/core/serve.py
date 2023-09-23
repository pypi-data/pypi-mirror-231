from itertools import chain, zip_longest
from pancake.__core__ import *
from pancake.tools.managers import *
from pancake.tools.wrappers import *

__all__: tuple = (
  "sift", "pile",
  "flip"
)

def sift(
  data: list[dict] | dict
) -> list[dict]:
  ...
  if type(data) is dict:
    ...
    data = [data]
  
  data = list(map(dict.items, data))
  data = list(map(tuple, data))
  data = list(set(data))
  data = list(map(dict, data))
  
  #TODO: Can be better
  uniques: list[dict] = []
  
  for dat in data:
    ...
    if len(dat) > 0:
      ...
      uniques += [dat]
  
  return uniques  

def pile(
  data: list[dict] | dict,
  priorities: list[dict] | dict
) -> list[dict]:
  ...
  #TODO: Can make better - try using builtin groupby
  if type(data) is dict:
    ...
    data = [data]
  
  if type(priorities) is dict:
    ...
    priorities = [priorities]
    
  for group in priorities:
    ...
    grps: dict = __gather(group)
    priorities: list = list(grps.values()).sort()
    
    for priority in priorities:
      ...
      for key in grps:
        ...
        if grps[key] == priority:
          ...
          data = __groupby(data, key)
          
  return data

def flip(
  data: list[dict] | dict[str, list]
) -> dict[str, list] | list[dict] | None:
  ...
  with (
    Binding(list, mapping, func=Binding(list, dict.items)) as __items,
    Binding(list, mapping, func=Binding(list, zip_longest)) as __zip,
    Binding(list, chain) as __chain
  ):
    ...
    if type(data) is list:
      ...
      data = __chain(*__items(data))
      
      data = {
        key: [
          val
          for k, val in data
          if k == key
        ]
        for key, _ in data
      }
    
    elif type(data) is dict:
      ...
      keys, [*data] = __zip(*dict.items(data))
      
      data = [
        {
          key: val
          for key, val in d
        }
        for d in __zip(
          keys * len(data),
          data
        )
      ]
      
    return data
  
  # inverts: list[dict] | dict[str, list] | None = None
  
  # if type(data) is list:
  #   ...
  #   inverts = defaultdict(list)
      
  #   for d in data:
  #     ...
  #     for key, val in d.items():
  #       ...
  #       inverts[key] += [val]
        
  # elif type(data) is dict:
  #   ...
  #   inverts = []

  #   ks, vals = zip(*data.items())

  #   for vs in zip(*vals):
  #     ...
  #     inverts += [
  #       {k: v for k, v in zip(ks, vs)}
  #     ]
  
  # return inverts
  