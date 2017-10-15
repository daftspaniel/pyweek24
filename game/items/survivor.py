import arcade

from game.constants import GAME_WIDTH, GAME_HEIGHT
from game.util import RND


class Survivor(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.angle = 0
        self.turn = False
        self.wobble = True
        self.speed = RND(3)

    def update(self):
        if self.turn and RND(20) == 1:
            self.angle += RND(5) - 1
        if self.wobble:
            if RND(5) == 1:
                self.center_x += RND(5) - 1
            if RND(5) == 1:
                self.center_y += RND(5) - 1
        super().update()

        # Wrap round screen
        self.center_x = self.center_x % GAME_WIDTH
        self.center_y = self.center_y % GAME_HEIGHT
