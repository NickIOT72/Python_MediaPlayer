# Kivy Libraries
import kivy # Impor kivy librarir
from kivy.config import Config #Congiguration of Screen Prop
from kivy.core.window import Window # Config Window
from kivy.app import App # Set App on kivy Screen
from kivy.uix.screenmanager import ScreenManager, Screen # Set Screenmanahger to select screen and Screen to develop interface
import os
import threading
import time

########## Import files############
from screens.myscreenmanager import MyScreenManager
from screens.templates.Windows_Dim import  WindowDim

######### Code ############
class MusicPlayerApp(App):

    def build(self):

        return MyScreenManager()

def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print("%s: %s" % ( threadName, time.ctime(time.time()) )) 

if __name__ == "__main__":
    
    MusicPlayerApp().run()