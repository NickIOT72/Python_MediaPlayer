import pyaudio
import wave
from pydub import AudioSegment
import pygame, time
from pygame import mixer 

class MPS(object):

    StatusPlay = False
    StatusInit = False
    StatusSound = False

    def __init__(self):
        self.StatusPlay = False
        self.StatusInit = False
        self.StatusSound = False
        try:
            self.StatusInit = True
            pygame.init()
            pygame.mixer.init(frequency=44100, size=16, channels=2, buffer=4096)
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
        print("Pressed BUtton")
        soundfile = '_numb-official-video-linkin-park.mp3'
        if self.StatusInit == False:
            pygame.init()
            pygame.init()
            pygame.mixer.init(frequency=44100, size=16, channels=2, buffer=4096)
            self.StatusInit = True
            # Setting the volume 
            
        if self.StatusSound == False:
            pygame.mixer.music.set_volume(0.5) 
            clock = pygame.time.Clock()
            pygame.mixer.music.load(soundfile)
            pygame.mixer.music.play()
            self.StatusSound = True
        if self.StatusPlay == True:
            mixer.music.pause()
            self.StatusPlay = False
        elif self.StatusPlay == False:
            mixer.music.unpause()
            self.StatusPlay = True

    def stopmusic(self):
        """stop currently playing music"""
        if self.StatusSound == True:
            pygame.mixer.music.stop()
            self.StatusPlay = False
            self.StatusSound = False

    def getmixerargs(self):
        pygame.mixer.init()
        freq, size, chan = pygame.mixer.get_init()
        return freq, size, chan

    def initMixer(self):
        print("Initiation")
        pygame.init()
        pygame.mixer.init(frequency=44100, size=16, channels=2, buffer=4096)
        self.StatusInit = True

M = MPS()
M.playmusic()