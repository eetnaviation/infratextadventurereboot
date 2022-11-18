from Objects.Position import Position
from typing import TypeVar
from config import config
import os

T = TypeVar('T')
POSITION: str = ""
LEVEL: str = ""
LEVELS: list[T] = []

class Level(object):
  name: str = ""
  positions: list[Position] = []

  def __init__(self: T, name: str):
    global LEVELS
    self.name = name

    LEVELS.append(self)
  
  def addPosition(self: T, position: Position) -> T:
    self.positions.append(position)
    return self

  @staticmethod
  def setPosition(pos: str):
    global POSITION
    POSITION = pos
    return None
  
  @staticmethod
  def setLevel(level: str):
    global LEVEL
    LEVEL = level
    return None
  
  @staticmethod
  def promptUser():
    global LEVEL, POSITION
    level: Level = None
    position: Position = None

    if config["clear-screen"]:
      os.system('cls' if os.name == 'nt' else 'clear')
    if config["debug-messages"]:
      print("Position on prompt: " + LEVEL + ":" + POSITION)

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
          command.use()

    return None