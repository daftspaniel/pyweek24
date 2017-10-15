import arcade
import os

from game.constants import *
from game.player import Rescueboat

class Game(arcade.Window):
    def __init__(self):
        super().__init__(GAME_WIDTH, GAME_HEIGHT)
        self.setupSprites()
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    def setupSprites(self):
        self.player = Rescueboat(os.path.join('img', 'boat.png'), 2)
        self.boats = arcade.SpriteList()
        self.boats.append(self.player)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player.change_angle = 3
        elif symbol == arcade.key.RIGHT:
            self.player.change_angle = -3
        elif symbol == arcade.key.UP:
            self.player.thrust = 0.15
        elif symbol == arcade.key.DOWN:
            self.player.thrust = -.2

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player.change_angle = 0
        elif symbol == arcade.key.RIGHT:
            self.player.change_angle = 0
        elif symbol == arcade.key.UP:
            self.player.thrust = 0
        elif symbol == arcade.key.DOWN:
            self.player.thrust = 0

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(50, 100, 45,
                                  arcade.color.ALLOY_ORANGE)
        self.boats.draw()

    def update(self, x):
        self.boats.update();
