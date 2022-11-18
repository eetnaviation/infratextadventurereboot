from typing import Callable
from typing import TypeVar

T = TypeVar('T')

class Command(object):
  label: str
  shortId: str
  onUse: Callable[[], None]
  predicate: Callable[[], bool]

  onUseMoveToLevel: str = None
  onUseMoveToPosition: str = None

  def __init__(self: T, label: str, shortId: str="", onUse: Callable[[], None]=lambda:(), predicate: Callable[[], bool]=lambda:True):
    self.label = label
    self.shortId = shortId
    self.onUse = onUse
    self.predicate = predicate
  
  def onUse(self: T, onUse: Callable[[], None]) -> T:
    self.onUse = onUse
    return self
  
  def moveToLevel(self: T, level: str) -> T:
    self.onUseMoveToLevel = level
    return self
  
  def moveToPosition(self: T, position: str) -> T:
    self.onUseMoveToPosition = position
    return self

  def predicate(self: T, predicate: Callable[[], bool]) -> T:
    self.predicate = predicate
    return self

  def use(self: T):
    self.onUse()
    if self.onUseMoveToLevel != None:
      setLevel(self.onUseMoveToLevel)
    if self.onUseMoveToPosition != None:
      setPosition(self.onUseMoveToPosition)
    
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