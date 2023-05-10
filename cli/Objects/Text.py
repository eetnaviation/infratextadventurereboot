from typing import Callable
from typing import TypeVar

T = TypeVar('T')

class Text(object):
  predicate: Callable[[], bool]
  label: str

  def __init__(self: T, predicate: Callable[[], bool], label: str):
    self.predicate = predicate
    self.label = label
    return

  def __str__(self: T) -> str:
    return self.label
  
  def print(self: T):
    if self.predicate():
      print(self.label)

  def getLabel(self: T):
    if self.predicate():
      return self.label
    else:
      return None