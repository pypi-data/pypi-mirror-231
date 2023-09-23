from concurrent.futures import ThreadPoolExecutor
from pancake.tools.managers import Binding
from pancake.__core__ import *

__all__: tuple = (
  "strain", "extract", "smooth",
  "spread", "relabel"
)

def strain(
  data: list[dict] | dict,
  conditions: list[dict] | dict
) -> list[dict]:
  ...
  if type(data) is dict:
    ...
    data = [data]
    
  with (
    Binding(list, ThreadPoolExecutor().map) as map,
    Binding(__strain, conditions=conditions) as con
  ):
    ...
    data = map(con, data)
  
  #TODO: Can make this better
  strains: list[dict] = []
  
  for dat in data:
    ...
    if len(dat) > 0:
      ...
      strains += [dat]
  
  return strains

def extract(
  data: list[dict] | dict,
  extractions: list[dict] | dict
) -> list[dict]:
  ...
  if type(data) is dict:
    ...
    data = [data]
    
  with (
    Binding(list, ThreadPoolExecutor().map) as map,
    Binding(__extract, extractions=extractions) as ext
  ):
    ...
    data = map(ext, data)
  
  return data

# def smooth(
#   data: Iterable[Iterable]
# ) -> list[dict]:
#   ...
#   t: type = type(data)
  
#   if t in (set, list, tuple):
#     ...
#     data = __reduce(
#       data,
#       container = t()
#     ) or data
    
#   return data

def spread(
  data: list[dict] | dict,
  applications: list[dict] | dict
) -> list[dict]:
  ...
  if type(data) is dict:
    ...
    data = [data]
    
  with (
    Binding(list, ThreadPoolExecutor().map) as map,
    Binding(__applyto, applications=applications) as app
  ):
    ...
    data = map(app, data)
  
  return data

def relabel(
  data: list[dict] | dict,
  attributes: list[dict] | dict
) -> list[dict]:
  ...
  if type(data) is dict:
    ...
    data = [data]
    
  with (
    Binding(list, ThreadPoolExecutor().map) as map,
    Binding(__relabel, attributes=attributes) as lbl
  ):
    ...
    data = map(lbl, data)

  #TODO: Can make better
  relabels: list[dict] = []
  
  for dat in data:
    ...
    if len(dat) > 0:
      ...
      relabels += [dat]
  
  return relabels
