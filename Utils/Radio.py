from Objects.Level import Level
from Objects.Position import Position
from Objects.DocumentPosition import DocumentPosition
from Objects.Command import Command
from pygame.mixer import Sound
from sound import getSong
from threading import Thread
from time import sleep
import config
import pygame
import random


class Radio:

  playingMusic: bool = False
  currentSong: Sound = None
  songs: list[str] = []

  def __init__(self, songs: list[str]):
    self.songs = songs
  
  def toggle(self):
    if self.playingMusic == True:
      self.currentSong.stop()
      self.playingMusic = False
    else:
      self.nextSong()
  
  def nextSong(self):
    self.currentSong = getSong(random.choice(self.songs))
    self.currentSong.play()
    self.playingMusic = True

    def delay():
      sleep(self.currentSong.get_length())
      if self.playingMusic:
        self.nextSong()
    Thread(target=delay).start()