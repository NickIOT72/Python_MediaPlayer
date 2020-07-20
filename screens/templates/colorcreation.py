class ColorCreation:

    def __init__(self):
        pass
        
    def CreateColor(self,text):
        ColorArray = []
        for i in range(0,6,2):
            ColorArray[i/2] = int(int(text[i])*16 + int(text[i+1]))
        ColorArray[3] = 1
        ColorTuple = (ColorArray[0], ColorArray[1], ColorArray[2], ColorArray[3])
        ColorObj = {
            'rgba': ColorArray,
            'CanvasRGBA': ColorTuple
        }
        return ColorObj