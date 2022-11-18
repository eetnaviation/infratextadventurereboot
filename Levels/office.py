from Objects.Level import Level
from Objects.Position import Position
from Objects.Command import Command

grabbedGear = False

def grabGear():
  global grabbedGear
  grabbedGear = True

Level("office")\
  .addPosition(Position("intro")\
    .addText("You start your day like you start everyday, you are at work in a meeting.")
    .addText("Your Boss (Paul) is telling you and your co-workers where you are going to be inspecting today, You are going to be inspecting the Hammer Valley Dam.")
    .addCommand(Command(shortId="leave", label="Leave").moveToPosition("7th-floor-hallway"))
  )\
  .addPosition(Position("7th-floor-hallway")\
    .addText("You are in the main hallway on the 7th floor. Your co-workers stand there and are talking about public transport and how the tunnels aren't going to suddenly collapse.")
    .addText("You see a door labeled Sauna and an elevator.")
    .addCommand(Command(shortId="elevator", label="Go to the elevator and go to the 8th floor").moveToPosition("8th-floor-hallway"))
    .addCommand(Command(shortId="sauna", label="Go to the Sauna").moveToPosition("sauna-bottom"))
    #Maybe achievement?
    .addCommand(Command(shortId="suicide", label="Jump into the aura and commit suicide."))
  )\
  .addPosition(Position("8th-floor-hallway")\
    .addText("You are in the main hallway on the 8th floor.")
    .addText("You see a door and an elevator. Also your office is on this floor.")
    .addCommand(Command(shortId="door", label="Go through the door").moveToPosition("sauna-top"))
    .addCommand(Command(shortId="office", label="Go to your office").moveToPosition("office"))
    .addCommand(Command(shortId="elevator", label="Go to the elevator and go to the 7th floor", predicate=lambda:(not grabbedGear)).moveToPosition("7th-floor-hallway"))
    .addCommand(Command(shortId="elevator", label="Go to the elevator and go to the first floor", predicate=lambda:grabbedGear).moveToPosition("elevator-broken"))
    #Maybe achievement?
    .addCommand(Command(shortId="suicide", label="Jump into the aura and commit suicide."))
  )\
  .addPosition(Position("office")\
    .addText("You are in your office. You take a look at your tasks for today and grab your gear.")
    .addText("You get to know that you will visit a small Powerplant and later on the Bermann tunnels.")
    .addCommand(Command(shortId="leave", label="Leave", onUse=lambda:(grabGear())).moveToPosition("8th-floor-hallway"))
  )\
  .addPosition(Position("sauna-bottom")\
    .addText("You enterted the Sauna. You are now in a meeting room called Siemens, however you see some stairs.")
    .addCommand(Command(shortId="leave", label="Leave the Sauna").moveToPosition("7th-floor-hallway"))
    .addCommand(Command(shortId="stairs", label="Go up the stairs").moveToPosition("sauna-top"))
  )\
  .addPosition(Position("sauna-top")\
    .addText("You enterted the changing room. You can see a door with an exit sign and the Sauna itself. There is also a toilet to be found and some stairs.")
    .addCommand(Command(shortId="leave", label="Leave the Sauna").moveToPosition("8th-floor-hallway"))
    .addCommand(Command(shortId="stairs", label="Go down the stairs").moveToPosition("sauna-bottom"))
  )\
  \
  .addPosition(Position("elevator-broken")\
    .addText("Looks like there was a power outage. You are stuck in the elevator, however you see a fuse box.")
    .addCommand(Command(shortId="fuses", label="Fix fuses and leave").moveToPosition("3rd-floor-hallway"))
  )\
  .addPosition(Position("3rd-floor-hallway")\
    .addText("You are in the main hallway on the third floor.")
    .addText("You see many doors to numerous companies, a fire exit door and the top floor of the cafeteria.")
    .addCommand(Command(shortId="fireexit", label="Go to the fire exit").moveToPosition("3rd-floor-fireexit"))
    .addCommand(Command(shortId="cafeteria", label="Go to the cafeteria").moveToPosition("cafeteria-top"))
  )\
  .addPosition(Position("3rd-floor-fireexit")\
    .addText("You are in the fire exit on the 3rd floor. The way upstairs is blocked, but you can go downstairs.")
    .addCommand(Command(shortId="leave", label="Leave").moveToPosition("3rd-floor-hallway"))
    .addCommand(Command(shortId="down", label="Go downstairs").moveToPosition("2nd-floor-fireexit"))
  )\
  .addPosition(Position("2nd-floor-hallway")\
    .addText("You are in the main hallway on the second floor.")
    .addText("You construction workings, a fire exit door and the cafeteria.")
    .addCommand(Command(shortId="fireexit", label="Go to the fire exit").moveToPosition("2nd-floor-fireexit"))
    .addCommand(Command(shortId="cafeteria", label="Go to the cafeteria").moveToPosition("cafeteria-bottom"))
  )\
  .addPosition(Position("2nd-floor-fireexit")\
    .addText("You are in the fire exit on the 2nd floor.")
    .addCommand(Command(shortId="leave", label="Leave").moveToPosition("2nd-floor-hallway"))
    .addCommand(Command(shortId="up", label="Go upstairs").moveToPosition("3rd-floor-fireexit"))
    .addCommand(Command(shortId="down", label="Go downstairs").moveToPosition("1st-floor-fireexit"))
  )\
  .addPosition(Position("1st-floor-fireexit")\
    .addText("You are in the fire exit on the 1st floor.")
    .addCommand(Command(shortId="leave", label="Leave and enter reception").moveToPosition("reception"))
    .addCommand(Command(shortId="outside", label="Leave and go outside").moveToPosition("outside"))
    .addCommand(Command(shortId="up", label="Go upstairs").moveToPosition("2nd-floor-fireexit"))
    .addCommand(Command(shortId="down", label="Go downstairs to the parking garage").moveToPosition("garage"))
  )\
  .addPosition(Position("outside")\
    .addText("You are outside and you have found a geocache.")
    .addCommand(Command(shortId="leave", label="Go back inside").moveToPosition("1st-floor-fireexit"))
  )\
  .addPosition(Position("cafeteria-top")\
    .addText("You are in the top part of the cafeteria on the 3rd floor. You can go downstairs or to the main hallway.")
    .addCommand(Command(shortId="hallway", label="Go to the main hallway").moveToPosition("3rd-floor-hallway"))
    .addCommand(Command(shortId="stairs", label="Go downstairs").moveToPosition("cafeteria-bottom"))
  )\
  .addPosition(Position("cafeteria-bottom")\
    .addText("You are in the bottom part of the cafeteria on the 2nd floor. You see stairs and the kitchen.")
    .addText("You also see the main hallway.")
    .addCommand(Command(shortId="hallway", label="Go to the main hallway").moveToPosition("2nd-floor-hallway"))
    .addCommand(Command(shortId="stairs", label="Go upstairs").moveToPosition("cafeteria-bottom"))
    .addCommand(Command(shortId="kitchen", label="Go to kitchen").moveToPosition("kitchen"))
  )\
  .addPosition(Position("kitchen")\
    .addText("You are in the kitchen of the cafeteria. You can go to the eating area.")
    .addText("In the kitchen there is also a small office and a fire exit.")
    .addCommand(Command(shortId="office", label="Go into office").moveToPosition("kitchen-office"))
    .addCommand(Command(shortId="fireexit", label="Go to fire exit").moveToPosition("other-2nd-floor-fireexit"))
  )\
  .addPosition(Position("kitchen-office")
    .addText("You are in the kitchen office. There is a couch and a table with a newsletter form Stalburg Times.")
    .addText("The newslette says how NCG accidentially destroies a wrong buildings.")
    .addCommand(Command(shortId="leave", label="Leave").moveToPosition("kitchen"))
  )\
  .addPosition(Position("other-2nd-floor-fireexit")\
    .addText("You are in the other fire exit on the 2nd floor. The way upstairs is blocked but you can go downstairs.")
    .addCommand(Command(shortId="leave", label="Leave").moveToPosition("kitchen"))
    .addCommand(Command(shortId="down", label="Go downstairs").moveToPosition("other-1st-floor-fireexit"))
  )\
  .addPosition(Position("other-1st-floor-fireexit")\
    .addText("You are in the other fire exit on the 1st floor. You can go upstairs or leave.")
    .addCommand(Command(shortId="reception", label="Leave into the reception").moveToPosition("reception"))
    .addCommand(Command(shortId="serverroom", label="Leave into the server room").moveToPosition("server-room"))
    .addCommand(Command(shortId="up", label="Go upstairs").moveToPosition("other-2nd-floor-fireexit"))
  )\
  .addPosition(Position("server-room")\
    .addText("You are in the server room. You find a note which says: If you are reading this then congrats on getting out of that dumb game. Our servers have been hacked and the entire building is crazy.")
    .addText("You can go to the fire exit or the reception")
    .addCommand(Command(shortId="fireexit", label="Go to the fire exit").moveToPosition("other-1st-floor-fireexit"))
    .addCommand(Command(shortId="reception", label="Go to the reception").moveToPosition("reception"))
  )\
  .addPosition(Position("reception")
    .addText("You are at the reception. Your coworkers are talking about the power grid and you grab the master keys.")
    .addText("You can go to the server room, the fire exit next to it or the main fire exit.")
    .addCommand(Command(shortId="server", label="Go to the server room").moveToPosition("server-room"))
    .addCommand(Command(shortId="otherfireexit", label="Go to the fire exit next to the server room").moveToPosition("other-1st-floor-fireexit"))
    .addCommand(Command(shortId="fireexit", label="Go to the main fire exit").moveToPosition("1st-floor-fireexit"))
  )\
  .addPosition(Position("garage")
    .addText("You are in the parking garage. You can go back upstairs or go into your car.")
    .addCommand(Command(shortId="car", label="Enter your car").moveToLevel("reserve1"))
    .addCommand(Command(shortId="up", label="Go back upstairs").moveToPosition("1st-floor-fireexit"))
  )
