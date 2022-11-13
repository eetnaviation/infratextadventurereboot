from Objects.Level import Level
from Objects.Position import Position
from Objects.Command import Command

idk = False

def example():
    global idk
    idk = True

Level("office")\
  .addPosition(Position("0")\
    .addText("This will always show up.")
    .addCommand(Command(label="Set idk to true.", shortId="idk", onUse=example))
    .addCommand(Command(label="Progress", shortId="pr").moveToPosition("1"))
  )\
  .addPosition(Position("1")\
    .addTextPredicate(lambda: False, "This will never show up.")
    .addTextPredicate(lambda: idk, "This will show up once idk is True.")
    .addCommand(Command(label="Set idk to true", shortId="true", onUse=example))
    .addCommand(Command(label="Only shows if idk is true", predicate=lambda: idk).moveToPosition("0"))
  )
