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
from screens.templates.Slider_Layout import SliderTemplate, SliderBar
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
    #a = (ButtonPlayLayout.pos[0] + ButtonPlayLayout.width + WindowDim.Wsize_X*0.01 , ButtonPlayLayout.pos[1])
    #ButtonPauseLayout = ButtonTemplate( a)
    #ButtonPause = ButtonSet(1, ButtonPauseLayout)
    #ButtonPause.bind(on_press=lambda x:MusicSel.stopmusic('B') )
    #ButtonPauseLayout.add_widget(ButtonPause)
    #ButtonPlay.add_widget(ButtonPlay.ButtonD)
    # Button Pause Conf
    #a = (ButtonPlayLayout.pos[0] + ButtonPlayLayout.width + WindowDim.Wsize_X*0.01 , ButtonPlayLayout.pos[1])
    #ButtonPause = ButtonTemplate(1, a)
    # Button Stop Conf
    a = (ButtonPlayLayout.pos[0] + ButtonPlayLayout.width + WindowDim.Wsize_X*0.01 , ButtonPlayLayout.pos[1])
    ButtonStopLayout = ButtonTemplate( a)
    ButtonStop = ButtonSet(2, ButtonStopLayout)
    ButtonStop.bind(on_press=lambda x:MusicSel.stopmusic('A') )
    ButtonStopLayout.add_widget(ButtonStop)
    #ButtonStop.ButtonD.bind(on_press=MusicPlayer.stopmusic )
    # Button Rigth Conf
    a = (ButtonStopLayout.pos[0] + 2*ButtonStopLayout.width + 2*WindowDim.Wsize_X*0.03 , ButtonStopLayout.pos[1])
    ButtonNextLeftLayout = ButtonTemplate( a)
    ButtonNextLeft = ButtonSet(2, ButtonNextLeftLayout)
    ##ButtonNextLeft.bind(on_press=lambda x:MusicSel.NextLeftmusic('A') )
    ButtonNextLeftLayout.add_widget(ButtonNextLeft)
    #ButtonNextLeft.bind(on_press=MusicPlayer.LeftButton )
    # Button Left Conf
    a = (ButtonNextLeftLayout.pos[0] + ButtonNextLeftLayout.width + WindowDim.Wsize_X*0.01 , ButtonNextLeftLayout.pos[1])
    ButtonNextRightLayout = ButtonTemplate( a)
    ButtonNextRight = ButtonSet(2, ButtonNextRightLayout)
    ButtonNextRight.bind(on_press=lambda x:MusicSel.NextRightmusic('A') )
    ButtonNextRightLayout.add_widget(ButtonNextRight)
    #ButtonNextRight.bind(on_press=MusicPlayer.RitghButton )
    ########################################################################
    #Create FloatLayout to insert Slider
    b = ButtonNextRightLayout.pos[0] + ButtonNextRightLayout.size[0] - WindowDim.Wsize_X*0.03 
    P = (WindowDim.Wsize_X*0.03 , WindowDim.Wsize_Y*0.15 )
    Sz = (b , WindowDim.Wsize_Y*0.07 )
    Sense = 'horizontal'
    SongSliderLayout = SliderTemplate(P, Sz)
    SongSlider = SliderBar(SongSliderLayout, Sense, ColorList.Red.rgba)
    SongSliderLayout.add_widget(SongSlider)
    '''P = ((ButtonNextRight.pos[0] + ButtonNextRight.size[0]) + WindowDim.Wsize_Y*0.02 , ButtonNextLeft.pos[1] )
    b = WindowDim.Wsize_X*0.96 - (ButtonNextRight.pos[0] + ButtonNextRight.size[0])
    Sz = (b , ButtonNextRight.size[1]/2 )
    VolSliderLayout = SliderTemplate(P, Sz, Sense, ColorList.DarkBlue.rgba)
    ##############################
    
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
    #layout.add_widget(ButtonPauseLayout)
    layout.add_widget(ButtonStopLayout)
    #layout.add_widget(ButtonNextRight)
    #layout.add_widget(ButtonNextLeft)
    layout.add_widget(SongSliderLayout)
    #layout.add_widget(VolSliderLayout)
    #layout.add_widget(LabelSongTrackBackground)
    #layout.add_widget(LabelSongTrackTitle)
    #layout.add_widget(LabelVolBackground)
    #layout.add_widget(LabelVolTitle)

    SliderSongVal = float

    def __init__(self, **kw):    
        super(HomePage,self).__init__(**kw)
        self.add_widget(self.layout)
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
    SongPos = ''
    timer=''
    PrintTimeSta = True
    TimeSlider = 0

    def __init__(self):
        super(MusicSel, self).__init__()
        self.Mus = ''
        self.timer= threading.Thread(target= MusicSel.print_time)
        self.timer.start()

    print ('Caught KeyboardInterrupt')
    @staticmethod
    def playmusic(a):
        """Stream music with mixer.music module in blocking manner.
           This will stream the sound from disk while playing.
        """
        if (MusicSel.Mus):
            print("State: %s" % MusicSel.Mus)
            print("State %s" % MusicSel.Mus.state)
        if (MusicSel.SongPos):
            print("Pos: %s" % MusicSel.SongPos)
        else:
            print("SongPos Empty")

        if True: #not MusicSel.Mus or MusicSel.SongPos or (MusicSel.Mus and (MusicSel.Mus.get_pos() == 0.00) ):
            if not MusicSel.Mus or (MusicSel.Mus and (not MusicSel.SongPos)  and MusicSel.Mus.state == 'stop') :
                path = os.getcwd() + '\screens\music\myfile.wav'
                sound = SoundLoader.load(path)
                MusicSel.Mus = sound
                MusicSel.Mus.play()
                MusicSel.Mus.seek(MusicSel.Mus.length -7)
                HomePage.SongSlider.max = 7.0
                HomePage.SongSlider.min = 0.0
                HomePage.SongSlider.value = 0.0
                HomePage.SliderSongVal = float(7)
                time.sleep(0.01)
                #print("Play1")
            elif (MusicSel.Mus) and MusicSel.Mus.state == 'play':
                MusicSel.pausemusic('h')
            elif (MusicSel.Mus and MusicSel.Mus.state == 'stop'):
                if not MusicSel.SongPos and (MusicSel.Mus.get_pos() == 0.00) :
                    MusicSel.Mus.stop()
                    MusicSel.Mus = ''
                    MusicSel.SongPos = ''
                else:
                    #print("Sound found at %s" % MusicSel.Mus.source)
                    #print("Sound is %.3f seconds" % MusicSel.Mus.length)
                    MusicSel.Mus.play()
                    path = os.getcwd() + '\screens\images' + '\PlayButton_Down_2.png'
                    path1 = os.getcwd() + '\screens\images' + '\PlayButton_On_2.png'
                    HomePage.ButtonPlay.background_normal = path
                    HomePage.ButtonPlay.background_down = path1
                if MusicSel.SongPos:
                    MusicSel.Mus.seek(MusicSel.SongPos)
                    MusicSel.SongPos = ''

    @staticmethod
    def pausemusic(a):
        """Stream music with mixer.music module in blocking manner.
           This will stream the sound from disk while playing.
        """
        if MusicSel.Mus:
            #print(MusicSel.Mus.state)
            if MusicSel.Mus.state == 'play':
                #print("Sound found at %s" % MusicSel.Mus.source)
                #print("Stopped")
                MusicSel.SongPos = MusicSel.Mus.get_pos()
                #print("Time: %s " % MusicSel.SongPos)
                MusicSel.Mus.stop()
                path = os.getcwd() + '\screens\images' + '\Pause_Button_Normal_2.png'
                path1 = os.getcwd() + '\screens\images' + '\Pause_Button_Down_2.png'
                HomePage.ButtonPlay.background_normal = path
                HomePage.ButtonPlay.background_down = path1
                #MusicSel.Mus = ''
        #print("Error: unable to start thread")

    @staticmethod
    def stopmusic(a):
        if MusicSel.Mus:
            MusicSel.Mus.stop()
            MusicSel.Mus = ''
            MusicSel.SongPos = ''
            path = os.getcwd() + '\screens\images' + '\PlayButton_Down_2.png'
            path1 = os.getcwd() + '\screens\images' + '\PlayButton_On_2.png'
            HomePage.ButtonPlay.background_normal = path
            HomePage.ButtonPlay.background_down = path1
    
    @staticmethod 
    def print_time():
        count = 0
        while MusicSel.PrintTimeSta:
            if (MusicSel.Mus):
                A = MusicSel.Mus.get_pos() - (MusicSel.Mus.length -7)
                if A >= 7:
                    A = 7
                if A <= 0:
                    A = 0
                print("Time: %s " % A)
                HomePage.SongSlider.value = A
            time.sleep(0.05)