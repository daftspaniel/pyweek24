import math
import arcade

from game.common.constants import GAME_WIDTH, GAME_HEIGHT
from game.common.util import RND


class Heli(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.angle = 0
        self.speed = 1

    def update(self):
        super().update()
        self.change_y = 3

        if self.center_y >660:
            self.center_x = 100 + RND(GAME_WIDTH)
            print(self.center_x)

        # Wrap round screen
        self.center_x = self.center_x % GAME_WIDTH
        self.center_y = self.center_y % (GAME_HEIGHT * 2 + RND(100))
