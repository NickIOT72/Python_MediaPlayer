class ColorCreation():

    def __init__(self, colortext):
        ColorArray = [0,0,0,1]
        for i in range(0,3):
            ColorArray[i] = (float(int(colortext[i*2],16)*16 + int(colortext[i*2+1],16) )/255)
        ColorArray[3] = 1
        ColorTuple = (ColorArray[0], ColorArray[1], ColorArray[2], ColorArray[3])
        self.rgba = ColorArray
        self.CanvasRGBA = ColorTuple

class ColorList():
    Black = ColorCreation('000000')
    Night = ColorCreation('0C090A')
    BlueIvy = ColorCreation('3090C7')
    LightSeaGreen = ColorCreation("3EA99F")
    White = ColorCreation("FFFFFF")