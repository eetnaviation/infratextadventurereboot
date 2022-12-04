from Objects.Position import Position
from typing import TypeVar
from config import config
import os
import inquirer

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
    if POSITION != "":
      Level.getPosition(Level.getLevel(LEVEL), POSITION).onLeave()
    POSITION = pos
    Level.getPosition(Level.getLevel(LEVEL), POSITION).onVisit()
    return None
  
  @staticmethod
  def setLevel(level: str):
    global LEVEL
    LEVEL = level
    return None
  
  @staticmethod
  def getLevel(name) -> T:
    toReturn = None
    for level1 in LEVELS:
      if level1.name == name:
        toReturn = level1
    return toReturn
  
  @staticmethod
  def getPosition(level: T, name: str) -> Position:
    toReturn = None
    for position1 in level.positions:
      if (position1.name == name):
        toReturn = position1
    return toReturn
  
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

    choices: list[str] = []
    for command in position.commands:
      if command.predicate():
        choices.append(command.label)
    
    prompt = inquirer.prompt([inquirer.List("action", message="Next action:", choices=choices)])
    
    if prompt == None:
      raise Exception("")

    for command in position.commands:
      if command.predicate():
        if command.label == prompt["action"]:
          command.use()

    return None