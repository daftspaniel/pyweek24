import math

import arcade

from game.constants import *
from game.util import keepWithinRange, RND


class Rescueboat(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.center_x = 222
        self.center_y = 333
        self.angle = 0
        self.thrust = 0
        self.speed = 0
        self.top_speed = 3
        self.waterdrag = 0.05
        self.obstacles = []
        self.trail = []

    def update(self):
        self.manageDrag()

        self.speed = keepWithinRange(self.speed + self.thrust, -self.top_speed, self.top_speed)

        self.change_x = -math.sin(math.radians(self.angle)) * self.speed
        self.change_y = math.cos(math.radians(self.angle)) * self.speed

        if self.change_x + self.change_y == 0:
            super().update()
            if len(self.trail) > 0 and RND(4) == 1: self.trail.pop(0)
            return

        x = self.center_x
        y = self.center_y

        self.center_x += self.change_x
        self.center_y += self.change_y
        #
        # if arcade.geometry.check_for_collision(self, self.wall):
        #     self.center_x = x
        #     self.center_y = y
        #     self.change_x = 0
        #     self.change_y = 0
        #
        # Wrap round screen
        self.center_x = self.center_x % GAME_WIDTH
        self.center_y = self.center_y % GAME_HEIGHT

        if len(self.trail) < 42 and RND(2) == 1:
            self.trail.append([self.center_x + RND(3), self.center_y + RND(3)])
            self.trail.append([self.center_x - RND(3), self.center_y - RND(3)])
        if len(self.trail) > 41:
            self.trail.pop(0)

        super().update()

    def manageDrag(self):
        if self.speed > 0:
            self.speed -= self.waterdrag
            if self.speed < 0:
                self.speed = 0
        if self.speed < 0:
            self.speed += self.waterdrag
            if self.speed > 0:
                self.speed = 0
