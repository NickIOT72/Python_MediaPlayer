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
import tkinter as tk
from tkinter import filedialog
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
        Color(rgba = ColorList.MarbleBlue.CanvasRGBA )
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
    # Button Search
    a = (ButtonPlayLayout.pos[0] + WindowDim.Wsize_X*0.01 , LabelBodyBackground.pos[1] + LabelBodyBackground.size[1] 
        - ButtonPlayLayout.size[1] - WindowDim.Wsize_Y*0.01  )
    ButtonSearchLayout = ButtonTemplate( a)
    ButtonSearch = ButtonSet(5, ButtonSearchLayout)
    ButtonSearch.bind(on_press=lambda x:MusicSel.Searchmusic('A') )
    ButtonSearchLayout.add_widget(ButtonSearch)
    #Create SearchTitle Background
    LabelSearchTitleBackground = Label(
        pos = (ButtonSearchLayout.pos[0] + ButtonSearchLayout.size[0] + WindowDim.Wsize_X*0.01, 
            ButtonSearchLayout.pos[1] ), 
        size = ( WindowDim.Wsize_Y*0.9 , ButtonSearchLayout.size[1])
    )
    with LabelSearchTitleBackground.canvas:
        Color(rgba = ColorList.BlueIvy.CanvasRGBA )
        Rectangle(pos=LabelSearchTitleBackground.pos, size=LabelSearchTitleBackground.size)
    #Create Title Label 
    SearchLabelTitle = Label(
        text = '<- Select Song', 
        color = ColorList.White.rgba,
        pos = LabelSearchTitleBackground.pos, 
        size = LabelSearchTitleBackground.size,
        size_hint = (None,None),
        font_size = '30sp')
    ########################################################################
    #Create FloatLayout to insert Slider
    b = ButtonNextRightLayout.pos[0] + ButtonNextRightLayout.size[0] - WindowDim.Wsize_X*0.03 
    P = (WindowDim.Wsize_X*0.03 , WindowDim.Wsize_Y*0.15 )
    Sz = (b , WindowDim.Wsize_Y*0.07 )
    Sense = 'horizontal'
    SongSliderLayout = SliderTemplate(P, Sz)
    SongSlider = SliderBar(SongSliderLayout, Sense, ColorList.Red.rgba)
    SongSlider.bind(on_touch_down= lambda x1,x2:MusicSel.SliderTouch('A') )
    SongSliderLayout.add_widget(SongSlider)
    P = ((ButtonNextRight.pos[0] + ButtonNextRight.size[0]) + WindowDim.Wsize_Y*0.02 , ButtonNextLeft.pos[1] )
    b = WindowDim.Wsize_X*0.96 - (ButtonNextRight.pos[0] + ButtonNextRight.size[0])
    Sz = (b , ButtonNextRight.size[1]/2 )
    #VolSliderLayout = SliderTemplate(P, Sz, Sense, ColorList.DarkBlue.rgba)
    VolSliderLayout = SliderTemplate(P, Sz)
    VolSlider = SliderBar(VolSliderLayout, Sense, ColorList.DarkBlue.rgba)
    VolSlider.bind(on_touch_up= lambda x1,x2:MusicSel.SliderVolTouch('A') )
    VolSliderLayout.add_widget(VolSlider)

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
        Rectangle(pos=LabelSongTrackBackground.pos, size=LabelSongTrackBackground.size)
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
    layout.add_widget(ButtonSearchLayout)
    layout.add_widget(SongSliderLayout)
    layout.add_widget(VolSliderLayout)
    layout.add_widget(LabelSongTrackBackground)
    layout.add_widget(LabelSongTrackTitle)
    layout.add_widget(LabelVolBackground)
    layout.add_widget(LabelVolTitle)
    layout.add_widget(LabelSearchTitleBackground)
    layout.add_widget(SearchLabelTitle)

    SliderSongVal = float

    def __init__(self, **kw):    
        super(HomePage,self).__init__(**kw)
        self.add_widget(self.layout)
        MusicSel()

        #self.layout.add_widget(self.FadeButton(on_press=self.fadeAnimation) )
        #self.fadeAnimation()
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

    PrintTimeSta = True
    ActionNumber = 0
    SelectedSong = ''
    SongLastPos = ''
    RSlider = 0
    RSlider2 = 0
    file_path = ''

    def __init__(self):
        super(MusicSel, self).__init__()
        HomePage.VolSlider.value = 50
        HomePage.LabelVolTitle.text = "Vol: " + str(HomePage.VolSlider.value) + "%"
        self.timer= threading.Thread(target= MusicSel.print_time)
        self.timer.start()

    #print ('Caught KeyboardInterrupt')
    @staticmethod
    def playmusic(a):
        if (MusicSel.file_path):
            if not MusicSel.SelectedSong:
                MusicSel.ActionNumber = 1
            else:
                if MusicSel.SelectedSong.state == 'stop' :
                    MusicSel.ActionNumber = 2
                else:
                    MusicSel.ActionNumber = 3
  
    @staticmethod
    def stopmusic(a):
        if MusicSel.SelectedSong:
            MusicSel.ActionNumber = 4
    
    @staticmethod 
    def SliderTouch(a):
        MusicSel.RSlider = MusicSel.RSlider +1
        if (MusicSel.RSlider >= 1):
            if (MusicSel.SelectedSong):
                MusicSel.ActionNumber = 5
            #else:
            #    HomePage.SongSlider.value = 0
            MusicSel.RSlider = 0

    @staticmethod
    def SliderVolTouch(a):
        MusicSel.RSlider2 = MusicSel.RSlider2 + 1
        if (MusicSel.RSlider2 >= 1):
            if (MusicSel.SelectedSong):
                MusicSel.SelectedSong.volume = round(HomePage.VolSlider.value/100,2)
            MusicSel.RSlider2 = 0
    
    @staticmethod
    def Searchmusic(a):
        root = tk.Tk()
        root.withdraw()
        MusicSel.file_path = str(filedialog.askopenfilename())
        print(MusicSel.file_path)
        if (MusicSel.file_path):
            SongFormat = MusicSel.file_path.split(".")
            if (SongFormat[len(SongFormat) -1] == "wav"):
                print("Es wav")
                y = MusicSel.file_path.split("/")
                y1 = y[len(y) -1]
                y2 = y1.split(".")
                filename = y2[0]
                HomePage.SearchLabelTitle.text = "File: " + filename
                MusicSel.ActionNumber = 1
            else:
                MusicSel.file_path=''

    @staticmethod 
    def print_time():
        count = 0
        while MusicSel.PrintTimeSta:
            if (MusicSel.ActionNumber == 1 or MusicSel.ActionNumber == 2 ):
                MusicSel.PlaySong(MusicSel.ActionNumber)
            elif (MusicSel.ActionNumber == 3 ):
                MusicSel.PauseSong()
            elif (MusicSel.ActionNumber == 4 ):
                MusicSel.StopSong()
            elif (MusicSel.ActionNumber == 5 ):
                MusicSel.SongSliderTracker()
            if not (MusicSel.ActionNumber == 0):
                MusicSel.ActionNumber = 0
            HomePage.LabelVolTitle.text = "Vol: " + str(int(HomePage.VolSlider.value)) + "%"
            if (MusicSel.SelectedSong):
                HomePage.LabelSongTrackTitle.text =(str(int(HomePage.SongSlider.value/60)).zfill(2)
                + ":" + str(int(HomePage.SongSlider.value%60)).zfill(2) + ":"
                + str(int(HomePage.SongSlider.max/60)).zfill(2) + ":" 
                + str(int(HomePage.SongSlider.max%60)).zfill(2)) 
            else:
                HomePage.LabelSongTrackTitle.text = "0:00/0:00"
            if (MusicSel.SelectedSong):
                if MusicSel.SelectedSong.state == 'play':
                    HomePage.SongSlider.value = MusicSel.SelectedSong.get_pos()
                else:
                    if (MusicSel.SongLastPos):
                        HomePage.SongSlider.value = MusicSel.SongLastPos
            
            time.sleep(0.01)
    
    @staticmethod 
    def PlaySong(a):
        #MusicSel.stopmusic('A')
        if (a == 2):
            MusicSel.SelectedSong.stop()
            if (MusicSel.ActionNumber == 2):
                path = os.getcwd() + '\screens\images' + '\PlayButton_Down_2.png'
                path1 = os.getcwd() + '\screens\images' + '\PlayButton_On_2.png'
                HomePage.ButtonPlay.background_normal = path
                HomePage.ButtonPlay.background_down = path1
        if (a == 1):
            path = MusicSel.file_path
            sound = SoundLoader.load(path)
            MusicSel.SelectedSong = sound
        MusicSel.SelectedSong.play()
        if (a == 2):
            if MusicSel.SongLastPos:
                MusicSel.SelectedSong.seek(MusicSel.SongLastPos)
                MusicSel.SongLastPos = ''
        MusicSel.SelectedSong.volume = round(HomePage.VolSlider.value/100,2)
        if (a == 1):
            HomePage.SongSlider.max = MusicSel.SelectedSong.length
            HomePage.SongSlider.min = 0.0
            HomePage.SongSlider.value = 0.0
            #time.sleep(0.01)

    @staticmethod 
    def PauseSong():
        MusicSel.SongLastPos = MusicSel.SelectedSong.get_pos()
        MusicSel.SelectedSong.stop()
        path = os.getcwd() + '\screens\images' + '\Pause_Button_Normal_2.png'
        path1 = os.getcwd() + '\screens\images' + '\Pause_Button_Down_2.png'
        HomePage.ButtonPlay.background_normal = path
        HomePage.ButtonPlay.background_down = path1
    
    @staticmethod 
    def StopSong():
        MusicSel.SelectedSong.stop()
        MusicSel.SelectedSong = ''
        MusicSel.SongLastPos = ''
        path = os.getcwd() + '\screens\images' + '\PlayButton_Down_2.png'
        path1 = os.getcwd() + '\screens\images' + '\PlayButton_On_2.png'
        HomePage.ButtonPlay.background_normal = path
        HomePage.ButtonPlay.background_down = path1
        HomePage.SongSlider.value = HomePage.SongSlider.min
    
    @staticmethod 
    def SongSliderTracker():
        MusicSel.SongLastPos = HomePage.SongSlider.value
        if not MusicSel.SelectedSong.state == 'stop':
            MusicSel.PlaySong(2)
        