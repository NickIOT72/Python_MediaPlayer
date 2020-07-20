class ButtonElements:
    ButtonSize = ()
    ButtonPos = ()
    ButtonText = str
    ButtonColorText = []
    ButtonBGC = []
    ButtonBorder = []

    def __init__(self, ButtonSize, ButtonPos, ButtonText, ButtonColorText , ButtonBGC, ButtobBorder):
        self.ButtonText = ButtonText
        self.ButtonBGC = ButtonBGC
        self.ButtonBorder = ButtonBorder
        self.ButtonPos = ButtonPos
        self.ButtonColorText = ButtonColorText
        self.ButtonSize = ButtonSize
