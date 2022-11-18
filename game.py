import json
import os
import pygame
import sound
from Objects.Level import Level
from config import config

import Levels.office
import Levels.reserve1
import Levels.ending2

saveState = {}

def loadSave():
  global saveState
  saveFile: str = config["save-file"]
  saveState = {
  	"level": config["start-pos"]["level"],
    "position": config["start-pos"]["position"]
  }
  if os.path.exists(saveFile):
    f = open(saveFile)
    saveState = json.load(f)
    f.close()
    print(saveState["position"])
  else:
    writeSave()
  Level.setLevel(saveState["level"])
  Level.setPosition(saveState["position"])

def writeSave():
  global saveState
  f = open(config["save-file"], "w")
  f.write(json.dumps(saveState, indent=4))
  f.close()

loadSave()
sound.init()

while True:
  Level.promptUser()


#getSong("sound/music/action.wav").play()