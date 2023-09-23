from pancake.__core__ import *
from pancake.types.mapping import MapReturn

__all__: tuple = (
  "get", "flatten",
  "scatter", "spatter"
)

# def get(
#   inpath: list[str] | str
# ) -> list:
#   ...
#   if type(inpath) not in (list, str):
#     ...
#     return []
  
#   elif type(inpath) is str:
#     ...
#     inpath = [inpath]
  
#   data: list[dict] = []
  
#   with ThreadPoolExecutor() as pool:
#     ...
#     for d in list(pool.map(__get, inpath)):
#       ...
#       data += d
      
#   return data

def get(
  paths: list[str]
) -> list:
  ...
  if type(paths) is str:
    ...
    paths = [paths]
  
  __result: MapReturn = __get(paths)
  
  return __result
  
def flatten(
  data: list[dict]
) -> list[dict]:
  ...
  if type(data) is dict:
    ...
    data = [data]
  
  __result: MapReturn = (
    __flatten(data)
  )
  
  return __result
  
def scatter(
  data: list[dict]
) -> list[dict]:
  ...
  if type(data) is dict:
    ...
    data = [data]
  
  __result: MapReturn = (
    __scatter(data)
  )
  
  return __result
  
  # scats: list[dict] = []
  
  # with Bind(
  #   list,
  #   ThreadPoolExecutor().map
  # ) as map:
  #   ...
  #   for s in map(
  #     __scatter,
  #     data
  #   ):
  #     ...
  #     scats += s

  # return scats
  
  # with __Bind(
  #   simmer,
  #   list,
  #   ThreadPoolExecutor().map
  # ) as map:
  #   ...
  #   data = map(
  #     __scatter,
  #     data
  #   )

def spatter(
  data: list[dict] | dict
) -> list[dict]:
  ...
  if type(data) is dict:
    ...
    data = [data]
  
  __result: MapReturn = (
    __spatter(data)
  )
  
  return __result
    
  # with (
  #   __Bind(list, ThreadPoolExecutor().map) as map,
  #   __Bind(tuple, dict.keys) as tkeys
  # ):
  #   ...
  #   keys: set = set(map(
  #     tkeys,
  #     data
  #   ))
    
  #   data = map(partial(
  #     __spatter,
  #     keys=keys
  #   ), data)
    
  # return data
  