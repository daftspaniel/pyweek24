import math
import arcade

from game.common.constants import GAME_WIDTH, GAME_HEIGHT
from game.common.util import RND


class Shark(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.angle = RND(360)
        self.turn = False
        self.wobble = False
        self.speed = RND(3)

    def update(self):
        self.change_x = -math.sin(math.radians(self.angle)) * self.speed
        self.change_y = math.cos(math.radians(self.angle)) * self.speed
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
