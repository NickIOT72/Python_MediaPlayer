# Kivy Libraries
import kivy # Impor kivy librarir
from kivy.config import Config #Congiguration of Screen Prop
from kivy.core.window import Window # Config Window
from kivy.app import App # Set App on kivy Screen
from kivy.uix.screenmanager import ScreenManager, Screen # Set Screenmanahger to select screen and Screen to develop interface
import os

########## Import files############
from screens.myscreenmanager import MyScreenManager
from screens.templates.Windows_Dim import  WindowDim

######### Code ############
class MusicPlayerApp(App):

    def build(self):
        return MyScreenManager()

if __name__ == "__main__":

    MusicPlayerApp().run()