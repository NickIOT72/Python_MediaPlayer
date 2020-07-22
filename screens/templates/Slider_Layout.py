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

class SliderTemplate(FloatLayout):

    def __init__(self,  Pos, Size, **kwargs):
        super(SliderTemplate , self).__init__(**kwargs)
        self.pos = Pos
        self.size = Size
        with self.canvas:
            Color(rgba = ColorList.BlueIvy.CanvasRGBA )
            Rectangle(pos=self.pos, size=self.size)

class SliderBar(Slider):

    def __init__(self, FS,  Sense , TrackColor, **kwargs):
        super(SliderBar, self).__init__(**kwargs)
        self.value_track=True
        self.value_track_color=TrackColor
        self.min=0
        self.max=100
        self.value=0
        self.orientation= Sense
        self.size_hint = (None,None)
        self.size = FS.size
        self.pos_hint = FS.pos_hint
        self.pos = FS.pos
        self.step = 0.1
        # Add slider to Flayout
        #self.add_widget(SliderMusic)