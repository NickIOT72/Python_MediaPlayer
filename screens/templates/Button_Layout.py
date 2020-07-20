from kivy.properties import NumericProperty, StringProperty, BooleanProperty, ListProperty, ObjectProperty
from kivy.clock import Clock
from kivy.animation import Animation, AnimationTransition
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from screens.templates.colorlist import ColorList
from kivy.uix.slider import Slider
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window # Config Window
from screens.templates.Windows_Dim import  WindowDim
import os
import cv2
from PIL import Image

class ButtonTemplate(FloatLayout):

    def __init__(self, PathNum , **kw):
        super(ButtonTemplate, self).__init__(**kw)
        self.pos = (WindowDim.Wsize_X*0.03 , WindowDim.Wsize_Y*0.02 )
        self.size = (WindowDim.Wsize_X*0.13 , WindowDim.Wsize_Y*0.1 )
        with self.canvas:
            Color(rgba = ColorList.LightSeaGreen.rgba )
            Rectangle(pos=self.pos, size=self.size)
        
        
        ###############

        #Image processing
        path = os.getcwd() + '\screens\images'
        ######### Play Button
        ButtonPlayPath0 = path + '\PlayButton_Down.png'
        ButtonPlayPath1 = path + '\PlayButton_Down_2.png'
        ButtonPlayPath2 = path + '\PlayButton_On.png'
        ButtonPlayPath3 = path + '\PlayButton_On_2.png'
        ######## Pause Button
        ButtonPausePath0 = path + '\Pause_Button_Normal.png'
        ButtonPausePath1 = path + '\Pause_Button_Normal_2.png'
        ButtonPausePath2 = path + '\Pause_Button_Down.png'
        ButtonPausePath3 = path + '\Pause_Button_Down_2.png'
        ######## NextRight Button
        ButtonNextRightPath0 = path + '\RowNextRight_Button_Down.png'
        ButtonNextRightPath1 = path + '\RowNextRight_Button_Normal_2.png'
        ButtonNextRightPath2 = path + '\RowNextRight_Button_Down.png'
        ButtonNextRightPath3 = path + '\RowNextRight_Button_Down_2.png'
        ######## NextLeft Button
        ButtonNextLeftPath0 = path + '\RowNextLeft_Button_Normal.png'
        ButtonNextLeftPath1 = path + '\RowNextLeft_Button_Normal_2.png'
        ButtonNextLeftPath2 = path + '\RowNextLeft_Button_Down.png'
        ButtonNextLeftPath3 = path + '\RowNextLeft_Button_Down_2.png'
        ######## Stop Button
        ButtonStopPath0 = path + '\Stop_Button_Normal.png'
        ButtonStopPath1 = path + '\Stop_Button_Normal_2.png'
        ButtonStopPath2 = path + '\Stop_Button_Down.png'
        ButtonStopPath3 = path + '\Stop_Button_Down_2.png'
        ############## Path Array
        PathArray = [
            [ButtonPlayPath0, ButtonPlayPath1, ButtonPlayPath2, ButtonPlayPath3],
            [ButtonPausePath0, ButtonPausePath1, ButtonPausePath2, ButtonPausePath3],
            [ButtonStopPath0, ButtonStopPath1, ButtonStopPath2, ButtonStopPath3],
            [ButtonNextRightPath0, ButtonNextRightPath1, ButtonNextRightPath2, ButtonNextRightPath3],
            [ButtonNextLeftPath0, ButtonNextLeftPath1, ButtonNextLeftPath2, ButtonNextLeftPath3]
        ]
        #############
        #PathNum = 0
        Path1 = PathArray[PathNum][1]
        Path2 = PathArray[PathNum][3]
        # Resize Image
        im = Image.open(PathArray[PathNum][0])
        newsize = (int(self.width), int(self.height))
        # resize image
        new_image = im.resize(newsize)
        new_image.save(PathArray[PathNum][1])
        # Resize Image
        im = Image.open(PathArray[PathNum][2])
        newsize = (int(self.width), int(self.height))
        # resize image
        new_image = im.resize(newsize)
        new_image.save(PathArray[PathNum][3])
        ButtonD = Button(
            size_hint = (None,None),
            size = self.size,
            pos_hint = self.pos_hint,
            pos = self.pos,
            background_normal = Path1,
            background_down = Path2
        )
        self.add_widget(ButtonD)