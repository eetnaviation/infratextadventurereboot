from typing import TypeVar
from Objects.Position import Position
from Objects.Command import Command
from Objects.Text import Text
import save

T = TypeVar('T')

class DocumentPosition(Position):

  identifier: str
  parentPositon: str

  def __init__(self: T, name: str, identifier: str, parentPositon: str, text: str):
    self.name = name
    self.identifier = identifier
    self.parentPositon = parentPositon
    self.commands = [Command(shortId="b", label="Go back").moveToPosition(self.parentPositon)]
    self.texts = [Text(lambda: True, text)]

  def onVisit(self: T):
    if self.identifier not in save.discoveredDocuments:
      save.discoveredDocuments.append(self.identifier)
      print("Corruption score")
  