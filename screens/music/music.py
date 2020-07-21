import pyaudio
import wave
from pydub import AudioSegment
import pygame, time
from pygame import mixer 
import threading
import time

class MPS(object):

    StatusPlay = bool
    StatusInit = bool
    StatusSound = bool

    def __init__(self):
        self.StatusPlay = False
        self.StatusInit = False
        self.StatusSound = False
        try:
            #self.StatusInit = True
            #pygame.init()
            #pygame.mixer.init(frequency=44100, size=16, channels=2, buffer=4096)
            print("Initation")
        	#playmusic('_numb-official-video-linkin-park.mp3')
        except KeyboardInterrupt:	# to stop playing, press "ctrl-c"
            stopmusic()
            print("\nPlay Stopped by user")
        except Exception:
        	print("unknown error")

    def playmusic(self):
        """Stream music with mixer.music module in blocking manner.
           This will stream the sound from disk while playing.
        """
        print(self)


    def stopmusic(self):
        """stop currently playing music"""
        print("Stop Music")
    
    def LeftButton(self):
        """stop currently playing music"""
        print("Stop Music")
    
    def RitghButton(self):
        """stop currently playing music"""
        print("Stop Music")