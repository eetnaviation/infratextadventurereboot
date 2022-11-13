import json
from Levels.office import init
from Objects.Level import Level

levelspath = "Levels/"

file = open(levelspath+"start.json","rb")
start = json.loads(file.read().decode("utf-8-sig"))
file.close()

levelfile = start["file"]
position = start["position"]
currentlevel = ""
debugMode = 1

init()
while True:
	Level.promptUser()

exit()

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
	if command[0] == "next-level" and levelfile == "reserve2" and position == 9: levelfile = "reserve3"
    #Position change and commands
	if command[0] in level[position]["commands"]:
		position = level[position]["commands"][command[0]]
	else:
		print("You didn't know what to think of that action.\n")
