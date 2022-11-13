import json
import os
import vpk
import pygame
import Levels.office
from Objects.Level import Level
from config import config

infraPaths: list[str] = ["/home/" + os.getlogin() + "/.steam/debian-installation/steamapps/common/infra/"]
infraPath: str = None
musicVpk = None
saveState = {}

def initINFRA():
	global infraPaths, infraPath, musicVpk
	for path in config["additional-infra-paths"]:
		infraPaths.append(path)

	for path in infraPaths:
		if os.path.exists(path):
			print("Found INFRA path: " + path + ".")
			infraPath = path
			musicVpk = vpk.open(path + "infra/pak01_dir.vpk")
			pygame.mixer.init()

	if infraPath == None:
		print("No INFRA path found, sounds will be disabled.")
		config["sound-enabled"] = False

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
	else:
		writeSave()
	Level.setLevel(saveState["level"])
	Level.setPosition(saveState["position"])

def writeSave():
	global saveState
	f = open(config["save-file"], "w")
	f.write(json.dumps(saveState, indent=4))
	f.close()

def getSong(path):
	if musicVpk == None:
		return None
	if os.path.exists("tmp.wav"):
		os.remove("tmp.wav")
	tmpFile = open("tmp.wav", "wb")
	tmpFile.write(musicVpk.get_file(path).read())
	tmpFile.close()
	sound = pygame.mixer.Sound("tmp.wav")
	os.remove("tmp.wav")
	return sound

initINFRA()
loadSave()
getSong("sound/music/ambient.wav").play()

while True:
	Level.promptUser()