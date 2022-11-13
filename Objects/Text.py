from typing import Callable

class Text(object):
  predicate: Callable[[], bool]
  label: str

  def __init__(self, predicate: Callable[[], bool], label: str):
    self.predicate = predicate
    self.label = label
    return
  
  def getLabel(self):
    if self.predicate():
      return self.label
    else:
      return None