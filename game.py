import json
import os
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sound
from save import Save
from Objects.Level import Level
from config import config
import traceback

import Levels.office
import Levels.reserve1
import Levels.ending2

Save.loadSave()
sound.init()

try:
  while True:
    Level.promptUser()
except:
  Save.saveSave()
  traceback.print_exc()


#getSong("sound/music/action.wav").play()
