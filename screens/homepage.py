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
from screens.templates.Button_Layout import ButtonTemplate, ButtonSet
from screens.templates.Slider_Layout import SliderTemplate
from screens.music.music import MPS
import pyaudio
import wave
from pydub import AudioSegment
import pygame, time
from pygame import mixer 
import threading
import time
from kivy.core.audio import SoundLoader
#04246134112
#04146210791

#tracking 526438

class HomePage(Screen):

    layout = FloatLayout()
    #Create Title Label 
    LabelTitle = Label(
        text = 'Music Player', 
        color = ColorList.White.rgba,
        pos = (WindowDim.Wsize_X*0.01 , WindowDim.Wsize_Y*0.88 ), 
        size = (WindowDim.Wsize_X*0.98 , WindowDim.Wsize_Y*0.11 ),
        size_hint = (None,None),
        font_size = '60sp')
    #Create Title Background
    TabbedPanelTitleBackground = Label (
        pos = LabelTitle.pos, 
        size = LabelTitle.size,
    )
    with TabbedPanelTitleBackground.canvas:
        Color(rgba = ColorList.BlueIvy.CanvasRGBA )
        Rectangle(pos=TabbedPanelTitleBackground.pos, size=TabbedPanelTitleBackground.size)
    #Create Body Background
    LabelBodyBackground = Label(
        pos = (WindowDim.Wsize_X*0.01 ,WindowDim.Wsize_Y*0.27), 
        size = (WindowDim.Wsize_X*0.98,WindowDim.Wsize_Y*0.6)
    )
    with LabelBodyBackground.canvas:
        Color(rgba = ColorList.BlueIvy.CanvasRGBA )
        Rectangle(pos=LabelBodyBackground.pos, size=LabelBodyBackground.size)
    #Create Footer Background
    LabelFooterBackground = Label(
        pos = (WindowDim.Wsize_X*0.01 ,WindowDim.Wsize_Y*0.01), 
        size = (WindowDim.Wsize_X*0.98,WindowDim.Wsize_Y*0.25)
    )
    with LabelFooterBackground.canvas:
        Color(rgba = ColorList.MarbleBlue.CanvasRGBA )
        Rectangle(pos=LabelFooterBackground.pos, size=LabelFooterBackground.size)
    ##########################Creatr Button Layout################################## 
    ## Button Play Configuration
    a = (WindowDim.Wsize_X*0.03 , WindowDim.Wsize_Y*0.02 )
    ButtonPlayLayout = ButtonTemplate( a)
    ButtonPlay = ButtonSet(0, ButtonPlayLayout)
    ButtonPlay.bind(on_press=lambda x:MusicSel.playmusic('A') )
    ButtonPlayLayout.add_widget(ButtonPlay)
    ## Button Stop Configuration
    a = (ButtonPlayLayout.pos[0] + ButtonPlayLayout.width + WindowDim.Wsize_X*0.01 , ButtonPlayLayout.pos[1])
    ButtonPauseLayout = ButtonTemplate( a)
    ButtonPause = ButtonSet(1, ButtonPauseLayout)
    ButtonPause.bind(on_press=lambda x:MusicSel.stopmusic('B') )
    ButtonPauseLayout.add_widget(ButtonPause)
    #ButtonPlay.add_widget(ButtonPlay.ButtonD)
    # Button Pause Conf
    '''a = (ButtonPlay.pos[0] + ButtonPlay.width + WindowDim.Wsize_X*0.01 , ButtonPlay.pos[1])
    ButtonPause = ButtonTemplate(1, a)
    # Button Stop Conf
    a = (ButtonPause.pos[0] + ButtonPause.width + WindowDim.Wsize_X*0.01 , ButtonPause.pos[1])
    ButtonStop = ButtonTemplate(2,a)
    #ButtonStop.ButtonD.bind(on_press=MusicPlayer.stopmusic )
    # Button Rigth Conf
    a = (ButtonStop.pos[0] + ButtonStop.width + WindowDim.Wsize_X*0.03 , ButtonStop.pos[1])
    ButtonNextLeft= ButtonTemplate(3,a)
    #ButtonNextLeft.bind(on_press=MusicPlayer.LeftButton )
    # Button Left Conf
    a = (ButtonNextLeft.pos[0] + ButtonNextLeft.width + WindowDim.Wsize_X*0.01 , ButtonNextLeft.pos[1])
    ButtonNextRight = ButtonTemplate(4,a)
    #ButtonNextRight.bind(on_press=MusicPlayer.RitghButton )
    ########################################################################
    #Create FloatLayout to insert Slider
    b = ButtonNextRight.pos[0] + ButtonNextRight.size[0] - WindowDim.Wsize_X*0.03 
    P = (WindowDim.Wsize_X*0.03 , WindowDim.Wsize_Y*0.15 )
    Sz = (b , WindowDim.Wsize_Y*0.07 )
    Sense = 'horizontal'
    SongSliderLayout = SliderTemplate(P, Sz, Sense, ColorList.Red.rgba)
    P = ((ButtonNextRight.pos[0] + ButtonNextRight.size[0]) + WindowDim.Wsize_Y*0.02 , ButtonNextLeft.pos[1] )
    b = WindowDim.Wsize_X*0.96 - (ButtonNextRight.pos[0] + ButtonNextRight.size[0])
    Sz = (b , ButtonNextRight.size[1]/2 )
    VolSliderLayout = SliderTemplate(P, Sz, Sense, ColorList.DarkBlue.rgba)
    #Create Label Vol and Song Tarcker
    LabelVolTitle = Label(
        pos = (VolSliderLayout.pos[0] ,VolSliderLayout.pos[1] + VolSliderLayout.size[1] + WindowDim.Wsize_Y*0.01), 
        size = (VolSliderLayout.size[0],ButtonNextLeft.size[1]/2),
        text = 'Vol: 100%',
        color = ColorList.Black.rgba,
        size_hint = (None,None),
        font_size = '20sp'
    )
    LabelVolBackground = Label(
        pos = LabelVolTitle.pos, 
        size = LabelVolTitle.size
    )
    with LabelVolBackground.canvas:
        Color(rgba = ColorList.LightBlue.CanvasRGBA )
        Rectangle(pos=LabelVolBackground.pos, size=LabelVolBackground.size)
    LabelSongTrackTitle = Label(
        pos = (VolSliderLayout.pos[0] ,SongSliderLayout.pos[1]), 
        size = (LabelVolBackground.size[0], SongSliderLayout.size[1]),
        text = '0:00/0:00',
        color = ColorList.Black.rgba,
        size_hint = (None,None),
        font_size = '20sp'
    )
    LabelSongTrackBackground = Label(
        pos = LabelSongTrackTitle.pos, 
        size = LabelSongTrackTitle.size
    )
    with LabelSongTrackBackground.canvas:
        Color(rgba = ColorList.LightBlue.CanvasRGBA )
        Rectangle(pos=LabelSongTrackBackground.pos, size=LabelSongTrackBackground.size)'''
    # add labels to layout
    layout.add_widget(TabbedPanelTitleBackground)
    layout.add_widget(LabelTitle)
    layout.add_widget(LabelBodyBackground)
    layout.add_widget(LabelFooterBackground)
    layout.add_widget(ButtonPlayLayout)
    layout.add_widget(ButtonPauseLayout)
    #layout.add_widget(ButtonStop)
    #layout.add_widget(ButtonNextRight)
    #layout.add_widget(ButtonNextLeft)
    #layout.add_widget(SongSliderLayout)
    #layout.add_widget(VolSliderLayout)
    #layout.add_widget(LabelSongTrackBackground)
    #layout.add_widget(LabelSongTrackTitle)
    #layout.add_widget(LabelVolBackground)
    #layout.add_widget(LabelVolTitle)

    def __init__(self, **kw):    
        super(HomePage,self).__init__(**kw)
        self.add_widget(self.layout)
        self.stopmusic2()
        MusicSel()

        #self.layout.add_widget(self.FadeButton(on_press=self.fadeAnimation) )
        #self.fadeAnimation()

    def stopmusic2(self):
        print("Stop Music")
        return 1

    '''
    def fadeAnimation(self):
        self.TabbedPanelTitleBackground.pos = (698,430)
        anim = Animation( pos = (2 ,430), duration= 3, t='out_circ')
        anim.start(self.TabbedPanelTitleBackground)
    
    def compl(self, *args, **kws):
		pass
        #print("Complete Animation")
    '''

class MusicSel(object):

    PrintPlay = bool
    PrintPause = bool
    Mus = ''

    def __init__(self):
        super(MusicSel, self).__init__()
        self.Mus = ''
        #t = threading.Thread(name = "Timer" , target = self.print_time('Thr',2))
        #t.setDaemon(True)
        #t.start()

    @staticmethod
    def playmusic(a):
        """Stream music with mixer.music module in blocking manner.
           This will stream the sound from disk while playing.
        """
        if not MusicSel.Mus:
            path = os.getcwd() + '\screens\music\myfile.wav'
            sound = SoundLoader.load(path)
            MusicSel.Mus = sound
            print(MusicSel.Mus)
            if MusicSel.Mus and MusicSel.Mus.state == 'stop' :
                print("Sound found at %s" % MusicSel.Mus.source)
                print("Sound is %.3f seconds" % MusicSel.Mus.length)
                MusicSel.Mus.play()
            else:
                print("Error")

    @staticmethod
    def stopmusic(a):
        """Stream music with mixer.music module in blocking manner.
           This will stream the sound from disk while playing.
        """
        if MusicSel.Mus:
            print(MusicSel.Mus.state)
            if MusicSel.Mus.state == 'play':
                print("Sound found at %s" % MusicSel.Mus.source)
                print("Stopped")
                MusicSel.Mus.stop()
                MusicSel.Mus = ''
        #print("Error: unable to start thread")

    @staticmethod 
    def print_time( threadName, delay):
        count = 0
        while True:
            if MusicSel.PrintPlay:
                print("Print Play : True")
            else:
                print("Print Pause : False")
            if MusicSel.PrintPause:
                print("Print Play : True")
            else:
                print("Print Pause : False")
            time.sleep(delay)