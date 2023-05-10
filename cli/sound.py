from config import config
import os
import vpk
import pygame

musicVpk = None
infraPaths: list[str] = ["/home/" + os.getlogin() + "/.steam/debian-installation/steamapps/common/infra/"]
infraPath: str = None

def init():
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