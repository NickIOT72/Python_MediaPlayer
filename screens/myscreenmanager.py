from screens.homescreen import HomeScreen
from kivy.uix.screenmanager import ScreenManager, Screen # Set Screenmanahger to select screen and Screen to develop interface

class MyScreenManager(ScreenManager):

    def __init__(self, **kw):
        super(MyScreenManager,self).__init__(**kw)
        self.add_widget(HomeScreen(name='HomeScreen'))