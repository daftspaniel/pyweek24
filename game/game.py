from game.constants import *
from game.draw.location import *
from game.levels.levels import Levels
from game.player import Rescueboat
from game.util import imagePath


class Game(arcade.Window):
    def __init__(self):
        super().__init__(GAME_WIDTH, GAME_HEIGHT)
        self.levels = Levels()
        self.setupSprites()
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    def setupSprites(self):
        self.player = Rescueboat(imagePath('boat.png'), 2)
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
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.player.change_angle = 0
        elif symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.player.thrust = 0

    def on_draw(self):
        arcade.start_render()

        for point in self.player.trail:
            arcade.draw_circle_outline(point[0], point[1], 2, arcade.color.WHITE, 1)

        drawHome()

        self.boats.draw()
        self.levels.draw()

    def update(self, x):
        self.levels.update()
        self.boats.update()
