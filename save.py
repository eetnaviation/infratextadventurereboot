import os
import json
from config import config
from Objects.Level import Level

level: str
position: str
discoveredDocuments: list[str]

class Save:

  @staticmethod
  def loadSave():
    global level, position, discoveredDocuments

    saveFile: str = config["save-file"]

    level = config["start-pos"]["level"]
    position = config["start-pos"]["position"]
    discoveredDocuments = []

    if os.path.exists(saveFile):
      f = open(saveFile)
      loaded = json.load(f)
      
      level = loaded["level"]
      position = loaded["position"]
      discoveredDocuments = loaded["discoveredDocuments"]

      f.close()
    
    Level.setLevel(level)
    Level.setPosition(position)
  
  @staticmethod
  def saveSave():
    global level, position, discoveredDocuments

    f = open(config["save-file"], "w")
    f.write(json.dumps({
      "level": level,
      "position": position,
      "discoveredDocuments": discoveredDocuments
    }))
    f.close()