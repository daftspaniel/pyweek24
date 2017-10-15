from game.constants import *
from game.draw.location import *
from game.levels.levels import Levels
from game.player import Rescueboat
from game.util import imagePath


class Game(arcade.Window):
    def __init__(self):
        super().__init__(GAME_WIDTH, GAME_HEIGHT)
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
        self.levels = Levels()
        self.setupSprites()
        self.player.obstacles = self.levels.logs
        self.player.home = self.levels.home

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

        self.player.drawTrail()

        drawHome(self.player.passenger)

        self.boats.draw()
        self.levels.draw()

    def update(self, x):
        rescues = arcade.check_for_collision_with_list(self.player, self.levels.pickups)
        if len(rescues) > 0:
            for rescue in rescues:
                rescue.kill()
                self.player.passenger = True
        self.levels.update()
        self.boats.update()
