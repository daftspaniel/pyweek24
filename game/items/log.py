import arcade


class Log(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)