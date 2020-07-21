from screens.homepage import HomePage
from kivy.uix.screenmanager import ScreenManager, Screen # Set Screenmanahger to select screen and Screen to develop interface
from kivy.core.window import Window # Config Window

from screens.templates.Windows_Dim import  WindowDim

class HomeScreen(Screen):

    def __init__(self, **kw):
        super(HomeScreen,self).__init__(**kw)
        self.add_widget(HomePage(name="HomePage"))

