from Objects.Level import Level
from Objects.Position import Position
from Objects.DocumentPosition import DocumentPosition
from Objects.Command import Command
from Objects.Text import Text
from Utils.Radio import Radio
from save import Save, SaveData
from sound import getSong
import config

radio: Radio = Radio(["sound/music/action.wav", "sound/music/radio4.wav"])

Level("ending2")\
  .addPosition(Position("bed")\
    .addCommand(Command(shortId="radio", label="Toggle Readio", onUse=radio.toggle, predicate=lambda:config.config["sound-enabled"]))
    .addCommand(Command(shortId="ex", label="Goto example").moveToPosition(("example")))
  )
