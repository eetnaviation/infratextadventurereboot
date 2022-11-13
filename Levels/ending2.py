from Objects.Level import Level
from Objects.Position import Position
from Objects.Command import Command
from pygame.mixer import Sound
from sound import getSong
from threading import Thread
from time import sleep
import config
import pygame
import random

playingMusic: bool = False
currentSong: Sound = None
songs = ["sound/music/action.wav", "sound/music/radio4.wav"]

def toggleRadio():
  global playingMusic
  if playingMusic == True:
    currentSong.stop()
    playingMusic = False
  else:
    nextSong()

  print("Toggeling radio")

def nextSong():
  global currentSong, playingMusic
  currentSong = getSong(random.choice(songs))
  currentSong.play()
  playingMusic = True

  def delay():
    sleep(currentSong.get_length())
    if playingMusic:
      nextSong()
  Thread(target=delay).start()

Level("ending2")\
  .addPosition(Position("bed")\
    .addCommand(Command(shortId="radio", label="Toggle Readio", onUse=toggleRadio, predicate=lambda:config.config["sound-enabled"]))  
  )
