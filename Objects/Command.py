from typing import Callable
from typing import TypeVar

T = TypeVar('T')

class Command(object):
  label: str = None
  shortId: str = None
  onUse: Callable[[], None]  = None
  predicate: Callable[[], bool]  = None

  def __init__(self: T, label: str, shortId: str="", onUse: Callable[[], None]=lambda:(), predicate: Callable[[], bool]=lambda:True):
    self.label = label
    self.shortId = shortId
    self.onUse = onUse
    self.predicate = predicate
  
  def onUse(self: T, onUse: Callable[[], None]) -> T:
    self.onUse = onUse
    return self
  
  def moveToPosition(self: T, position: str) -> T:
    self.onUse = lambda: (
      setPosition(position)
    )
    return self
  
  def moveToLevel(self: T, level: str) -> T:
    self.onUse = lambda: (
      setLevel(level)
    )
    return self
  
  def predicate(self: T, predicate: Callable[[], bool]) -> T:
    self.predicate = predicate
    return self
  
  def getLabel(self: T):
    if self.predicate():
      return self.label
    else:
      return None

def setLevel(level):
  from Objects.Level import Level
  Level.setLevel(level)

def setPosition(pos):
  from Objects.Level import Level
  Level.setPosition(pos)