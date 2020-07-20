from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class LabelElements():
    L_text = str
    L_BGcolor = []
    L_color = []
    L_pos = ()
    L_size = ()
    L_sizehint = ()
    L_Form = str
    L_fontsize = str
    
    def __init__(self, L_text, L_color, L_BGcolor,  L_pos, L_size, L_sizehint, L_fontsize, L_Form):
        self.L_text = L_text
        self.L_color = L_color
        self.L_BGcolor = L_BGcolor
        self.L_pos = L_pos
        self.L_size = L_size
        self.L_sizehint = L_sizehint
        self.L_fontsize = L_fontsize
        self.L_Form = L_Form

    def SetLabelData(self):
        label = Label()
        label.text= self.L_text
        label.color = self.L_color[:]
        label.pos= self.L_pos
        label.font_size = self.L_fontsize
        label.size=self.L_size
        label.size_hint=self.L_sizehint
        label2 = Label()
        with label2.canvas:
            Color(self.L_BGcolor[0], self.L_BGcolor[1] , self.L_BGcolor[2] , self.L_BGcolor[3] )
            Rectangle(pos=label.pos, size=label.size)
        return label2, label 
