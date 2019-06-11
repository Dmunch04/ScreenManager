class ScreenPartion:
    def __init__ (this, X, Y, Width, Height, WidthPixelPosition, HeightPixelPosition):
        this.X = X
        this.Y = Y
        this.PositionID = (X, Y)

        this.Width = Width
        this.Height = Height

        this.WidthPixelPositionStart = WidthPixelPosition
        this.WidthPixelPositionEnd = WidthPixelPosition + Width
        this.HeightPixelPositionStart = HeightPixelPosition
        this.HeightPixelPositionEnd = HeightPixelPosition + Height

        # This is wrong
        this.Pixels = this.Width * this.Height

        this.ID = f'{X} {Y}'
        this.Name = f'Partion - {this.ID}'

    def __repr__ (this):
        return this.Name
