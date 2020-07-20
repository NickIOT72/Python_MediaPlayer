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
        Color(rgba = ColorList.BlueIvy.CanvasRGBA )
        Rectangle(pos=LabelFooterBackground.pos, size=LabelFooterBackground.size)
    
    ##########################Creatr Button Layout################################## 
    ButtonLayout = FloatLayout(
        pos = (WindowDim.Wsize_X*0.03 , WindowDim.Wsize_Y*0.02 ), 
        size = (WindowDim.Wsize_X*0.13 , WindowDim.Wsize_Y*0.1 ),
    )
    with ButtonLayout.canvas:
        Color(rgba = ColorList.LightSeaGreen.rgba )
        Rectangle(pos=ButtonLayout.pos, size=ButtonLayout.size)
    #Image processing
    path = os.getcwd()
    print(path)
    ButtonPlayPath = path + '\screens\images\PlayButton_Down.png'
    ButtonPlayPath2 = path + '\screens\images\PlayButton_Down_2.png'
    ButtonPlayPathOn = path + '\screens\images\PlayButton_On.png'
    ButtonPlayPathOn2 = path + '\screens\images\PlayButton_On_2.png'
    # Resize Image
    im = Image.open(ButtonPlayPath)
    newsize = (int(ButtonLayout.width), int(ButtonLayout.height))
    # resize image
    new_image = im.resize(newsize)
    new_image.save(ButtonPlayPath2)
    # Resize Image
    im = Image.open(ButtonPlayPathOn)
    newsize = (int(ButtonLayout.width), int(ButtonLayout.height))
    # resize image
    new_image = im.resize(newsize)
    new_image.save(ButtonPlayPathOn2)
    ButtonPlay = Button(
        size_hint = (None,None),
        size = ButtonLayout.size,
        pos_hint = ButtonLayout.pos_hint,
        pos = ButtonLayout.pos,
        background_normal = ButtonPlayPath2,
        background_down = ButtonPlayPathOn2
    )
    ButtonLayout.add_widget(ButtonPlay)
    ########################################################################
    #Create FloatLayout to insert Slider
    SliderLayout = FloatLayout(
        pos = (WindowDim.Wsize_X*0.03 , WindowDim.Wsize_Y*0.15 ), 
        size = (WindowDim.Wsize_X*0.5 , WindowDim.Wsize_Y*0.07 ),
    )
    with SliderLayout.canvas:
        Color(rgba = ColorList.BlueIvy.CanvasRGBA )
        Rectangle(pos=SliderLayout.pos, size=SliderLayout.size)
    SliderMusic = Slider(
        value_track=True, 
        value_track_color=[1, 0, 0, 1],
        min=0,
        max=100,
        value=25,
        orientation='horizontal',
        size_hint = (None,None),
        size = SliderLayout.size,
        pos_hint = SliderLayout.pos_hint,
        pos = SliderLayout.pos
    )
    # Add slider to Flayout
    SliderLayout.add_widget(SliderMusic)
    # add labels to layout
    layout.add_widget(TabbedPanelTitleBackground)
    layout.add_widget(LabelTitle)
    layout.add_widget(LabelBodyBackground)
    layout.add_widget(LabelFooterBackground)
    layout.add_widget(ButtonLayout)
    layout.add_widget(SliderLayout)
    
    def __init__(self, **kw):    
        super(HomePage,self).__init__(**kw)
        self.add_widget(self.layout)
        
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