from Objects.Level import Level
from Objects.Position import Position
from Objects.Command import Command

Level("reserve2")\
  .addPosition(Position("elevator")\
    .addText("You make your way down with the elevator. It suddenly breaks and you climb out. You see a security room.")
    .addCommand(Command(shortId="security-room", label="Enter security room").moveToPosition("security-room"))
  )\
  .addPosition(Position("security-room")\
    .addText("You enter the security-room. There is a door-control-panel and a light switch")
    .addCommand(Command(shortId="light-switch-sroom", label="Light switch").moveToPosition("light-switch-sroom"))
    .addCommand(Command(shortId="doors-panel", label="Door panel").moveToPosition("doors-panel"))
  )\
  .addPosition(Position("doors-panel")\
    .addText("You set all the doors to unlocked and leave. You see a door with a green light")
    .addCommand(Command(shortId="hallway-door", label="Door with green light").moveToPosition("hallway-door"))
  )\
  .addPosition(Position("light-switch-sroom")\
    .addText("You flick the light switch but nothing happens")
    .addCommand(Command(shortId="security-room", label="Continue").moveToPosition("security-room"))
  )\
  .addPosition(Position("hallway-door")\
    .addText("You enter the door with a green light and see shelves. The next room has a lab-door and a stairwell")
    .addCommand(Command(shortId="labdoor", label="Lab door").moveToPosition("labdoor"))
    .addCommand(Command(shortId="stairwell", label="Stairwell").moveToPosition("stairwell"))
  )\
  .addPosition(Position("labdoor")\
     .addText("The door is locked.")
    .addCommand(Command(shortId="hallway-door", label="Continue").moveToPosition("hallway-door"))
  )\
  .addPosition(Position("stairwell") \
    .addText("You go down the stairwell and photograph a leak. You head down a hallway and into the high-voltage switchboard area.")
    .addCommand(Command(shortId="power-lab", label="Unlock lab").moveToPosition("power-lab"))
    .addCommand(Command(shortId="power-turbine-hall", label="Electrify turbine hall").moveToPosition("power-turbine-hall"))
  )\
  .addPosition(Position("power-lab")\
    .addText("You turn on the power to the lab. You go up the stairwell and check out the lab.")
    .addText("The lab is being used to get beer to a perfect temperature.")
    .addCommand(Command(shortId="power-room-after-lab", label="Go back into the power room").moveToPosition("power-room-after-lab"))
  )\
  .addPosition(Position("power-room-after-lab")\
    .addText("You go down the stairwell back into the high-voltage switchroom.")
    .addCommand(Command(shortId="power-turbine-hall", label="Electrify turbine hall").moveToPosition("power-turbine-hall"))
  )\
  .addPosition(Position("power-turbine-hall")\
    .addText("You go through the flooded turbine hall, listen to hartman's speech, head through a sawmill and enter the cave.")
    .addCommand(Command(shortId="nextLevel", label="Head further into the cave").moveToLevel("reserve3"))
  )