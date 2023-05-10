from typing import Callable
from typing import TypeVar
from Objects.Command import Command
from Objects.Text import Text

T = TypeVar('T')

class Position(object):
  name: str
  commands: list[Command]
  texts: list[Text]

  def __init__(self: T, name: str):
    self.name = name
    self.commands = []
    self.texts = []
    return
  
  def addCommandSimple(self: T, onUse: Callable[[], None], label: str) -> T:
    self.addCommand(lambda: True, onUse, label)
    return self
  
  def addCommandFull(self: T, predicate: Callable[[], bool], onUse: Callable[[], None], label: str) -> T:
    self.addCommand(Command(label).onUse(onUse).predicate(predicate))
    return self
  
  def addCommand(self: T, command: Command) -> T:
    self.commands.append(command)
    return self


  def addText(self: T, text: str) -> T:
    return self.addTextPredicate((lambda: True), text)

  def addTextFull(self: T, text: Text) -> T:
    self.texts.append(text)
    return self

  def addTextPredicate(self: T, predicate: Callable[[], bool], text: str) -> T:
    return self.addTextFull(Text(predicate=predicate, label=text))
  
  
  def onVisit(self: T):
    return
  
  def onLeave(self: T):
    return