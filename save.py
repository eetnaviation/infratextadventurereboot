import os
import json
from config import config
from Objects.Level import Level

level: str = ""
position: str = ""
discoveredDocuments: list[str] = []
discoveredPhotos: list[str] = []
customData = dict()

class SaveData:

  key: str
  defaultValue: object

  def __init__(self, key: str, defaultValue: object):
    self.key = key
    self.defaultValue = defaultValue
  
  def getValue(self) -> object:
    global customData
    print(str(customData))

    if not self.key in customData:
      customData[self.key] = self.defaultValue
    
    return customData[self.key]
  
  def setValue(self, value):
    global customData
    customData[self.key] = value

class Save:

  @staticmethod
  def loadSave():
    global level, position, discoveredDocuments, discoveredPhotos, customData

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
      discoveredPhotos = loaded["discoveredPhotos"]
      customData = dict(loaded["customData"])

      f.close()
    
    Level.setLevel(level)
    Level.setPosition(position)
  
  @staticmethod
  def getData(key: str, defaultValue) -> SaveData:
    return SaveData(key, defaultValue)
  
  @staticmethod
  def saveSave():
    global level, position, discoveredDocuments, discoveredPhotos, customData

    f = open(config["save-file"], "w")
    f.write(json.dumps({
      "level": level,
      "position": position,
      "discoveredDocuments": discoveredDocuments,
      "discoveredPhotos": discoveredPhotos,
      "customData": customData
    }))
    f.close()

