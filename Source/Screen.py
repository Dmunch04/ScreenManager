import platform

from Source.ScreenPartion import ScreenPartion

class Screen:
    def __init__ (this, ScreenID = 1, Dimensions = ()):
        this.ScreenID = ScreenID

        if Dimensions != ():
            this.Width = Dimensions[0]
            this.Height = Dimensions[1]
            this.Dimensions = (this.Width, this.Height)

        else:
            this.Width = 1920
            this.Height = 1080
            this.Dimensions = (this.Width, this.Height)

            this.FindDimensions ()

        this.Partions = []

        this.DefinePartions ()

    def FindDimensions (this):
        Width = this.Width
        Height = this.Height

        if platform.system () == 'Linux':
            import subprocess

            Dimensions = subprocess.Popen (
                'xrandr | grep "\*" | cut -d" " -f4',
                shell = True,
                stdout = subprocess.PIPE
            ).communicate ()[0].decode ().split ('\n')[this.ScreenID - 1]

            Width, Height = Dimensions.split ('x')

        elif platform.system () == 'Windows':
            from win32api import GetSystemMetrics

            Width = GetSystemMetrics (0)
            Height = GetSystemMetrics (1)

        elif platform.system () == 'Darwin':
            from AppKit import NSScreen

            Width = NSScreen.mainScreen ().frame ().size.width
            Height = NSScreen.mainScreen ().frame ().size.height

        this.Width = int (Width)
        this.Height = int (Height)
        this.Dimensions = (int (Width), int (Height))

    def DefinePartions (this):
        Width = this.Width // 4
        Height = this.Height // 4
        Columns = this.Width // Width
        Rows = this.Height // Height

        # Old way of doing it:
        #this.Partions = [[ScreenPartion (Column, Row, Width, Height) for Column in range (Columns)] for Row in range (Rows)]

        Partions = []
        CurWidth = 0
        CurHeight = 0
        for Column in range (Columns):
            Partions.append ([])

            for Row in range (Rows):
                Partions[Column].append (ScreenPartion (Column, Row, Width, Height, CurWidth, CurHeight))

                CurHeight += Height

            CurWidth += Width
            CurHeight = 0

        this.Partions = Partions
