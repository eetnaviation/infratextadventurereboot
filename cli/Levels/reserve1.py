from Objects.Level import Level
from Objects.Position import Position
from Objects.DocumentPosition import DocumentPosition
from Objects.Command import Command
from Objects.Text import Text

POWERPLANT_NOTE = """Maintenance log
06.08.02: JK ---
20.08.02: JK A very hot day!
06.08.02: JK ---
03.09.02: JK ---
01.10.02: JK ---
14.10.02: JK ---
29.10.02: JK ---
05.11.02: JK Some weird pain in my chest?
19.11.02: JK ---
03.12.02: JK ---
16.12.02: JK ---
23.12.02: JK Holiday, here I come!
06.01.03:    NEW YEAR!
13.01.03: JK Heart aching again... Gotta take it slow...
27.01.03: JK ---
03.02.03: JK ---
17.02.03: JK ---
20.03.2003: JK To know I visted this shithole on a date like that is actually kinda sad...
~~~~~~~~~~~
26.08.03: JK Goddamn heart. Well at least this place is still intact.
08.09.03: JK After all this time I don't feel the same"""

SHACK_NOTE = """Note #1:
- Demand payment for sawmills massive log order (long overdue)
- Figure out how to pay our loan to the bank before we go bankrupt
- Get money to pay striking workers unpaid salleries
- Get new client

Note #2:
Matt,
Do you know why the dam stopped passing our logs through the chute?
It's been weeks since the last log passed through it.
I tried contacting the people at the dam to get this sorted out, but there's no one there.
Yesterday we tried to pushing the logs into the lug tunnel, but the chute seems to be blocked from the inside!
Any idea whats going on over there?
Also, I still have yet to recieve payment for the logs we sent you months ago.
- Tom

Note #3:
Dear Tom,
I know about the hydrocomapnies sudden bankrupcy, but I've seen Alex Hartman accasionally entering the
powerplant and light coming out of the windows of the damn at night.
As for the log payments, I'm still waiting for the funding from our client.
I'm expecting to receive the funding this week.
You'll recieve your share in chas then.
Sincerely, Matt

- reply to this soon
- demand payment
- get envelopes and stamps"""

HAS_BOLTCUTTERS = False
HAS_BOLTCUTTERS_NOT = True

def pickupBoltCutters():
  global HAS_BOLTCUTTERS, HAS_BOLTCUTTERS_NOT
  HAS_BOLTCUTTERS = True
  HAS_BOLTCUTTERS_NOT = False

Level("reserve1")\
  .addPosition(Position("car")\
    .addText("You just arrived. You look around. You see a small path leading under the bridge, and a bigger path going to a small power-plant.")\
    .addText("You give your boss a call and ask about last minute tips. He says to take pictures of everything that is broken and technical documents.")\
    .addCommand(Command(shortId="bridge", label="Go to bridge").moveToPosition("bridge"))\
    .addCommand(Command(shortId="pp", label="Go to the powerplant").moveToPosition(("powerplant-entrance")))
  )\
  .addPosition(Position("powerplant-entrance")\
    .addText("You are at the entrance of the power plant. You see a damaged mini-dam and are right next to the rivier.")
    .addCommand(Command(shortId="pp", label="Enter the powerplant").moveToPosition("powerplant-top-floor"))
    .addCommand(Command(shortId="leave", label="Go back to your car").moveToPosition(("car")))
  )\
  .addPosition(Position("powerplant-top-floor")\
    .addText("You are in the powerplant. You can go downstairs to the generators or go into the storage room.")
    .addText("You also find a note.")
    .addCommand(Command(shortId="generators", label="Go to the generators").moveToPosition("powerplant-bottom-floor"))
    .addCommand(Command(shortId="storage", label="Go to the storage room").moveToPosition("powerplant-storage"))
    .addCommand(Command(shortId="note", label="Look at the note").moveToPosition("powerplant-note"))
    .addCommand(Command(shortId="leave", label="Go back to the entrance").moveToPosition(("powerplant-entrance")))
  )\
  .addPosition(Position("powerplant-storage")\
    .addText("You are in the storage.")
    .addTextFull(Text(label="You see boltcutters.", predicate=lambda: HAS_BOLTCUTTERS_NOT))
    .addCommand(Command(shortId="boltcutters", label="Pick up boltcutters", predicate=lambda: HAS_BOLTCUTTERS_NOT, onUse=pickupBoltCutters))
    .addCommand(Command(shortId="leave", label="Go back to the main hall").moveToPosition("powerplant-top-floor"))
  )\
  .addPosition(Position("powerplant-bottom-floor")\
    .addText("You are at the generators. Looks like one is broken. You turn it off just to be safe.")
    .addTextFull(Text(label="You see an exit, however it is locked. You will need some boltcutters to open it.", predicate=lambda: HAS_BOLTCUTTERS_NOT))
    .addTextFull(Text(label="You see an exit, however it is locked. You have the boltcutters to open it.", predicate=lambda: HAS_BOLTCUTTERS))
    .addCommand(Command(shortId="leave", label="Go back upstairs").moveToPosition("powerplant-top-floor"))
    .addCommand(Command(shortId="leavepp", label="Exit the powerplant", predicate=lambda: HAS_BOLTCUTTERS).moveToPosition("powerplant-exit"))
  )\
  .addPosition(Position("powerplant-exit")\
    .addText("You are at the powerplant exit. You see a couple of bridges and a shack in the distance.")
    .addText("A path leads to the bridges and the shack.")
    .addCommand(Command(shortId="pp", label="Go back to the powerplant").moveToPosition("powerplant-bottom-floor"))
    .addCommand(Command(shortId="path", label="Follow the path").moveToPosition("before-morning-wood-shack"))
  )\
  .addPosition(Position("bridge")\
    .addText("You are at the other side of the bridge. You see water messurement device and a crack in one of the bridges pillars.")
    # TODO: Add stalburg water messurement devices
    .addCommand(Command(shortId="leave", label="Go back to your car").moveToPosition("car"))
  )\
  \
  .addPosition(Position("before-morning-wood-shack")\
    .addText("You are right next to the shack and the tow bridge. The door on the shack says '#12 Office MORNING WOOD CO. '")
    .addText("The first bridge leads to another path, altough you can not tell what is behind it due to the fog.")
    .addText("THe second bridge leads into a small hill, and you can not tell where it leads.")
    .addCommand(Command(shortId="shack", label="Enter the shack").moveToPosition("morning-wood-shack"))
    .addCommand(Command(shortId="pp", label="Go back to the powerplant").moveToPosition("powerplant-exit"))
    .addCommand(Command(shortId="bridgefog", label="Cross the bridge into the fog.").moveToPosition("railway-signal"))
    .addCommand(Command(shortId="bridgehill", label="Cross the bridge inro the hill.").moveToPosition("village"))
  )\
  .addPosition(Position("morning-wood-shack")\
    .addText("You are inside the small shack. You see a map and three notes.")
    .addCommand(Command(shortId="notes", label="Inspect the notes").moveToPosition("shack-notes"))
    .addCommand(Command(shortId="map", label="Inspect the map").moveToPosition("shack-map"))
    .addCommand(Command(shortId="leave", label="Leave the shack").moveToPosition("before-morning-wood-shack"))
  )\
  .addPosition(Position("railway-signal")\
    .addText("You are at a railway bridge. You see a rail signal which you turn off just to be save. You also see the hammer valley damn in the distance.")
    .addCommand(Command(shortId="small", label="Go back to the small bridge").moveToPosition("before-morning-wood-shack"))
    .addCommand(Command(shortId="cross", label="Cross the bridge").moveToPosition("railway-crossing"))
  )\
  .addPosition(Position("railway-crossing")\
    .addText("The railway crosses with a street. On one side you see a small village. On the other side of the road you see a dam entrance.")
    .addText("You also see a railway bridge which is near the actual dam.")
    .addCommand(Command(shortId="village", label="Go to the village.").moveToPosition("village"))
    .addCommand(Command(shortId="cross", label="Cross the bridge").moveToPosition("railway-signal"))
    .addCommand(Command(shortId="dam-entrance", label="Go to the dam entrance").moveToPosition("dam-entrance"))
  )\
  .addPosition(Position("village")\
    .addText("You are in the village. You see three houses but all are locked. There is also a broken power pole and you take a picture of it.")
    .addText("You can go down the path or go to a railway crossing")
    .addCommand(Command(shortId="path", label="Go down the path").moveToPosition(("before-morning-wood-shack")))
    .addCommand(Command(shortId="cross", label="Go to the railway crossing").moveToPosition(("railway-crossing")))
  )\
  .addPosition(Position("dam-entrance")\
    .addText("You are inside the dam entrence. You spot an elevator downstairs.")
    .addCommand(Command(shortId="leave", label="Go back to the railway crossing").moveToPosition("railway-crossing"))
    .addCommand(Command(shortId="elevator", label="Enter the elevator and go downstairs").moveToLevel("reserve2"))
  )\
  .addPosition(DocumentPosition("powerplant-note", "reserve1-powerplant-note", "powerplant-top-floor", POWERPLANT_NOTE))\
  .addPosition(DocumentPosition("shack-notes", "reserve1-shack-notes", "morning-wood-shack", SHACK_NOTE))\
  .addPosition(DocumentPosition("shack-map", "reserve1-shack-map", "morning-wood-shack", "A map where the logging zone is in red"))
