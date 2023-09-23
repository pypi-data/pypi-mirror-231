# from pancake.src.__core__ import *
# from pancake.tools.managers import *
# from pancake.tools.wrappers import *

# def prepare(
#   data: list | dict
# ) -> list:
#   ...
#   data = [
#     data
#   ] if (
#     type(
#       data
#     ) is dict
#   ) else data
  
#   with Binding(
#     spatter,
#     scatter,
#     flatten,
#     get
#   ) as prep:
#     ...
#     data = prep(data)
  
#   return data

# @mapping(container=[])
# def batch(
#   data: dict, *,
#   conditions: list[dict] | dict=None,
#   extractions: list[dict] | dict=None,
#   changes: list[dict] | dict=None,
#   attributes: list[dict] | dict=None,
#   container: list[dict]
# ) -> list[dict]:
#   ...
#   # kwargs: dict[str, list[dict] | dict] = {
#   #   "conditions": conditions,
#   #   "extractions": extractions,
#   #   "changes": changes,
#   #   "attributes": attributes
#   # }
  
#   with (
#     Binding(
#       relabel,
#       applyto,
#       extract,
#       strain,
#       attributes=attributes,
#       changes=changes,
#       extractions=extractions,
#       conditions=conditions,
#     ) as _batch
#   ):
#     ...
#   # container += 
#   # with (
#   #   Binding(
#   #     list,
#   #     ThreadPoolExecutor().map
#   #   ) as map,
#   #   Binding(
#   #     __batch,
#   #     **kwargs
#   #   ) as batch 
#   # ):
#   #   ...
#   #   data = map(batch, data)

#   # return data

# def serve(
#   data,
#   unique: bool=False,
#   priorities: dict=None,
#   invert: bool=False
# ) -> dict[str, list] | list[dict] | None:
#   ...
#   if unique:
#     ...
#     data = sift(data)
  
#     # __save(data[:100], "./Pancake/sift.json")
  
#   if priorities is not None:
#     ...
#     data = groupby(data, priorities)
    
#     # __save(data[:100], "./Pancake/groupby.json")
  
#   if invert:
#     ...
#     data = flip(data)
  
#     # __save(data, "./Pancake/flip.json")

# def make(
#   *,
#   inpath: list[str] | str=None,
#   outpath: str="./Pancake/cake.json",
#   purge: list[dict] | dict=None,
#   extract: list[dict] | dict=None,
#   change: list[dict] | dict=None,
#   priorities: list[str] | str=None,
#   attributes: list[dict] | dict=None,
#   unique: bool=False,
#   invert: bool=False
# ) -> list[dict]:
#   ...
#   data: list = get(inpath)
  
#   data = prepare(data)
#   # data = pat(
#   #   data=data,
#   #   conditions=conditions,
#   #   extractions=extractions,
#   #   attributes=attributes,
#   #   applyto=applyto,
#   #   priorities=groupby,
#   #   unique=unique,
#   #   # invert=invert
#   # )
  
#   data = batch(
#     data,
#     conditions=purge,
#     extractions=extract,
#     changes=change,
#     attributes=attributes
#   )
  
#   # if conditions is not None:
#   #   ...
#   #   data = strain(data, conditions)
    
#   #   __save(data[:100], "./Pancake/strain.json")
  
#   # if extractions is not None:
#   #   ...
#   #   data = extract(data, extractions)
    
#   #   __save(data[:100], "./Pancake/extract.json")
  
#   # if applications is not None:
#   #   ...
#   #   data = applyto(data, applications)
    
#   #   __save(data[:100], "./Pancake/applyto.json")
  
#   data = serve(
#     data,
#     unique=unique,
#     priorities=priorities,
#     invert=invert
#   )
  
#   # __save(data, "./Pancake/pat.json")
#   # data = bat(
#   #   data=data,
#   #   groupby=groupby,
#   #   unique=unique,
#   #   invert=invert
#   # )
#   # __save(data, "./Pancake/bat.json")
  
#   save(data, outpath)
  
#   return data

# # if __name__ == "__main__":
# #   ...
#   # data: list[dict] = make(
#   #   inpath=[
#   #     "./Data/SQuAD/dev-v2.0.json",
#   #     "./Data/QuAC/dev-v0.2.json"
#   #   ],
#   #   conditions=[
#   #     {
#   #       "paragraphs": {
#   #         "qas": {
#   #           "is_impossible": {
#   #             "$eq": False
#   #           }
#   #         }
#   #       }
#   #     },
#   #     {
#   #       "paragraphs": {
#   #         "qas": {
#   #           "answers": {
#   #             "text": {
#   #               "$ne": "CANNOTANSWER"
#   #             }          
#   #           }
#   #         }
#   #       }
#   #     }
#   #   ],
#   #   attributes=[
#   #     {
#   #       "paragraphs": {
#   #         "context": "context",
#   #         "qas": {
#   #           "question": "question",
#   #           "answers": {
#   #             "text": "answer"
#   #           }
#   #         }
#   #       }
#   #     }
#   #   ],
#   #   applyto=[
#   #     {
#   #       "paragraphs": {
#   #         "qas": {
#   #           "question": quest,
#   #           "answers": {
#   #             "text": stat
#   #           }
#   #         }
#   #       },
#   #       "question": quest,
#   #       "answer": stat
#   #     }
#   #   ],
#   #   # groupby=[
#   #   #   {
#   #   #     "$wi": [
#   #   #       {
#   #   #         "paragraphs": {
#   #   #           "context": 0
#   #   #         },
#   #   #         "context": 0
#   #   #       }
#   #   #     ]
#   #   #   }
#   #   # ],
#   #   unique=True,
#   #   # invert=True
#   # )
# data: list[dict] = make(
#   inpath="./Data/NewsQA/combined-newsqa-data-v1.json",
#   keep={
#     "questions": {
#       "isQuestionBad": {
#         "$eq": 0.0
#       },
#       "isAnswerAbsent": {
#         "$eq": 0.0
#       }
#     }
#   },
#   extract={
#     "answer": "$range",
#     "text": "$source",
#     "questions": {
#       "validatedAnswers": {
#         "s": "$start",
#         "e": "$end"
#       }
#     }
#   },
#   clean={
#     "questions": {
#       "q": strip
#     },
#     "answer": strip
#   },
#   select={
#     "text": "context",
#     "questions": {
#       "q": "question"
#     },
#     "answer": "answer"
#   },
#   group={
    
#   },
#   unique=True,
#   # invert=True
# )

# # {
# #   "answer": "$range",
# #   "text": "$source",
# #   "questions": {
# #     "validatedAnswers": {
# #       "s": "$start",
# #       "e": "$end"
# #     }
# #   },
# #   "summation": "$math:x*y",
# #   "questions": {
# #     "validatedAnswers": {
# #       "s": "$start",
# #       "e": "$end"
# #     }
# #   }
# # }