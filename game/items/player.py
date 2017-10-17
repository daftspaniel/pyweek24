import math
import arcade
from game.common.constants import *
from game.common.util import keepWithinRange, RND


class Rescueboat(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.top_speed = 3
        self.waterdrag = 0.05
        self.obstacles = []
        self.trail = []
        self.passenger = False

        self.alive = True
        self.score = 0
        self.boats = 3
        self.reset()

    def handleDeadlyCollision(self):
        if not self.alive: return
        self.alive = False
        self.boats -= 1
        self.passenger = False
        self.reset()

    def update(self):
        self.manageDrag()

        self.speed = keepWithinRange(self.speed + self.thrust, -self.top_speed, self.top_speed)
        self.change_x = -math.sin(math.radians(self.angle)) * self.speed
        self.change_y = math.cos(math.radians(self.angle)) * self.speed

        if self.change_x + self.change_y == 0:
            super().update()
            if len(self.trail) > 0 and RND(4) == 1: self.trail.pop(0)
            return

        self.alive = True
        home = self.checkIfBackHome()
        x = self.center_x
        y = self.center_y

        self.center_x += self.change_x
        self.center_y += self.change_y

        if not home:
            for obstacle in self.obstacles:
                if arcade.geometry.check_for_collision(self, obstacle):
                    self.center_x = x
                    self.center_y = y
                    self.change_x = 0
                    self.change_y = 0
                    break

        # Wrap round screen
        self.center_x = self.center_x % GAME_WIDTH
        self.center_y = self.center_y % GAME_HEIGHT

        self.updateTrail()

        if self.passenger and home:
            self.passenger = False
            self.score += 200

        super().update()

    def checkIfBackHome(self):
        return arcade.check_for_collision(self, self.home)

    def updateTrail(self):
        if len(self.trail) < 22 and RND(2) == 1:
            self.trail.append([self.center_x + RND(3), self.center_y + RND(3)])
            self.trail.append([self.center_x + RND(3), self.center_y + RND(3)])
        if len(self.trail) > 21:
            self.trail.pop(0)

    def drawTrail(self):
        for point in self.trail:
            arcade.draw_circle_outline(point[0], point[1], 2, arcade.color.WHITE, 1)

    def manageDrag(self):
        if self.speed > 0:
            self.speed -= self.waterdrag
            if self.speed < 0:
                self.speed = 0
        if self.speed < 0:
            self.speed += self.waterdrag
            if self.speed > 0:
                self.speed = 0

    def reset(self):
        self.angle = 0
        self.thrust = 0
        self.speed = 0
        self.trail = []
