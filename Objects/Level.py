from Objects.Position import Position
from typing import TypeVar
import os

POSITION: str = "0"
LEVEL: str = "office"
LEVELS: list = []
T = TypeVar('T')

class Level(object):
  name: str = ""
  positions: list[Position] = []

  def __init__(self: T, name: str):
    self.name = name

    LEVELS.append(self)
    return
  
  def addPosition(self: T, position: Position) -> T:
    self.positions.append(position)
    return self

  @staticmethod
  def setPosition(pos: str):
    global POSITION
    print("pos: " + pos)
    POSITION = pos
    return None
  
  @staticmethod
  def setLevel(level: str):
    global LEVEL
    LEVEL = level
    return None
  
  @staticmethod
  def promptUser():
    level: Level = None
    position: Position = None

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Position on prompt:" + POSITION)


    for level1 in LEVELS:
      if level1.name == LEVEL:
        level = level1
    for position1 in level.positions:
      if (position1.name == POSITION):
        position = position1

    for text in position.texts:
      if text.predicate():
        print(text.label)
    
    print("")

    print("Available Commands:")
    for command in position.commands:
      if command.predicate():
        print("- [" + command.shortId + "] " + command.label)
    
    prompt = input(">")

    for command in position.commands:
      if command.predicate():
        if command.label == prompt or command.shortId == prompt:
          if command.onUse != None:
            command.onUse()
    

    return None