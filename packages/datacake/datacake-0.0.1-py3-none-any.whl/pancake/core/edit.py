__all__: tuple = (
  "strip", "statement",
  "question"
)

def strip(
  phrase: str
) -> str:
  ...
  if type(phrase) is not str:
    ...
    return phrase
  
  phrase = phrase.replace("\"", "")
  
  while (
    len(phrase) > 0
    and phrase[0] in "\n\t ,.!?;"
  ):
    ...
    phrase = phrase[1:]

  if len(phrase) > 0:
    ...
    phrase = (
      phrase[0].upper()
      + phrase[1:]
    )
  
  while (
    len(phrase) > 0
    and phrase[-1] in "\n\t ,.!?;"
  ):
    ...
    phrase = phrase[:-1]
  
  return phrase

def statement(
  statement: str
) -> str:
  ...
  statement = (
    statement[0].upper()
    + statement[1:]
  )
  
  while (
    len(statement) > 0
    and statement[-1] in " ,.!?;"
  ):
    ...
    statement = statement[:-1]
  
  return statement

def question(
  question: str
) -> str:
  ...
  question = (
    question[0].upper()
    + question[1:]
  )
  
  if question[-1] in ".!":
    ...
    question = question[:-1] + "?"
  
  elif question[-1] not in "?":
    ...
    question = question + "?"
    
  return question
