from game.constants import *
import arcade
import math


class Rescueboat(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.center_x = 222
        self.center_y = 333
        self.angle = 0
        self.thrust = 0
        self.speed = 0
        self.top_speed = 2
        self.waterdrag = 0.05
        self.obstacles = []

    def update(self):
        if self.speed > 0:
            self.speed -= self.waterdrag
            if self.speed < 0:
                self.speed = 0

        if self.speed < 0:
            self.speed += self.waterdrag
            if self.speed > 0:
                self.speed = 0

        self.speed += self.thrust
        if self.speed > self.top_speed:
            self.speed = self.top_speed
        if self.speed < -self.top_speed:
            self.speed = -self.top_speed

        self.change_x = -math.sin(math.radians(self.angle)) * self.speed
        self.change_y = math.cos(math.radians(self.angle)) * self.speed

        if self.change_x + self.change_y == 0:
            super().update()
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
        self.center_x = self.center_x % GAME_WIDTH
        self.center_y = self.center_y % GAME_HEIGHT

        super().update()
