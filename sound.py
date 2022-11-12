import json
import vpk
import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import ctypes

levelspath = "Levels/"
infraPaths = "I:\Games\Steam\steamapps\common\INFRA"
infraPath = None
musicVpk = None
debugMode = 1

for path in infraPaths:
	if os.path.exists(path):
		infraPath = path

def getSong(song):
	if os.path.exists("tmp.wav"):
		os.remove("tmp.wav")
	tmpFile = open("tmp.wav", "wb")
	tmpFile.write(musicVpk.get_file("sound\music\cracks.wav").read())
	tmpFile.close()
	sound = pygame.mixer.Sound("tmp.wav")
	os.remove("tmp.wav")
	return sound

pygame.mixer.init()
if infraPath != None:
	print("Found INFRA Path: " + infraPath)
	musicVpk = vpk.open(infraPath + "\infra\pak01_dir.vpk")

	#getSong("sound/music/cracks.wav").play()
	#getSong("sound/music/furnace.wav").play()
else:
	ctypes.windll.user32.MessageBoxW(0, "ERR122 Game starting with no sounds!", "InfraTextAdventure-SoundParser", 0)

file = open(levelspath+"start.json","rb")
start = json.loads(file.read().decode("utf-8-sig"))
file.close()
levelfile = start["file"]
position = start["position"]
currentlevel = ""
while True:
	if levelfile != currentlevel:
		file = open(levelspath+levelfile+".json","rb")
		level = json.loads(file.read().decode("utf-8-sig"))
		file.close()
		currentlevel = levelfile
	#Print text from position
	print(level[position]["text"])
	#Show available commands
	print("\nAvailable Commands:",*[c+"," for c in level[position]["commands"]])
	
	if debugMode == 1: print("\nMap/Position", levelfile, position) #Debug data
	
	command = input(">").split(" ") #Get input for command
	#Level Movement
	if command[0] == "next-level" and levelfile == "office" and position == 15:
		levelfile = "reserve1"
	if command[0] == "next-level" and levelfile == "reserve1" and position == 12:
		levelfile = "reserve2"
		position = 0
	#Position change and commands
	if command[0] in level[position]["commands"]:
		position = level[position]["commands"][command[0]]
		if level[position]["playsound"]:
			getSong(level[position]["playsound"]).play()
	else:
		print("You didn't know what to think of that action.\n")