from tkinter import *

from ScreenManager.Screen import Screen

def DebugPartion (_Partion):
    print (_Partion.X, _Partion.Y)
    #print (Partion.Name)
    print (_Partion)
    print (f'Width: {_Partion.WidthPixelPositionStart} -> {_Partion.WidthPixelPositionEnd} || Height: {_Partion.HeightPixelPositionStart} -> {_Partion.HeightPixelPositionEnd}')
    print ('------------------------------------------')

def ScreenTest (_Screen):
    Width = _Screen.Width
    Height = _Screen.Height
    Partions = _Screen.Partions

    Root = Tk ()
    Root.title ('ScreenManager')
    Root.geometry (f'{Width}x{Height}')
    Root.resizable (False, False)

    _Canvas = Canvas (Root, width = Width, height = Height)
    _Canvas.pack ()

    Colors = [
        'red2',
        'blue2',
        'green2',
        'yellow2'
    ]
    TestColors = [
        [
            'red4',
            'red3',
            'red2',
            'red'
        ],

        [
            'blue4',
            'blue3',
            'blue2',
            'blue'
        ],

        [
            'green4',
            'green3',
            'green2',
            #'green'
            #'lawn green'
            'chartreuse2'
        ],

        [
            'yellow4',
            'yellow3',
            'yellow2',
            'yellow'
        ]
    ]
    TextColors = [
        'white',
        'white',
        'black',
        'black'
    ]

    for I, Column in enumerate (Partions):
        for J, Row in enumerate (Column):
            _Canvas.create_rectangle (
                Row.WidthPixelPositionStart,
                Row.HeightPixelPositionStart,
                Row.WidthPixelPositionEnd,
                Row.HeightPixelPositionEnd,
                #fill = Colors[I],
                fill = TestColors[I][J],
                outline = ''
            )

            X = Row.WidthPixelPositionEnd - (Width / 8)
            Y = Row.HeightPixelPositionEnd - (Height / 8)

            _Canvas.create_text (
                X,
                Y,
                text = Row.ID,
                #fill = 'white' if J == 0 else TextColors[I]
            )

    Root.mainloop ()

if __name__ == '__main__':
    #MyScreen = Screen ()                           # 1920x1080
    #MyScreen = Screen (Dimensions = (800, 600))    # 800x600
    MyScreen = Screen (Dimensions = (1280, 720))    # 1280x720

    ScreenTest (MyScreen)

    #for Column in MyScreen.Partions:
        #for Row in Column:
            #DebugPartion (Row)
            #print (Row.PositionID)
            #pass
