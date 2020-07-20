from kivy.core.window import Window # Config Window
from kivy.config import Config #Congiguration of Screen Prop

class WindowDim:
    
    Window.size = (700, 500)
    Window.clearcolor = (1, 1, 1, 1)
    Wsize_X = Window.width
    Wsize_Y = Window.height
    print(Wsize_X*0.01)
    print(Wsize_Y)