from game.constants import *
from game.draw.location import *
from game.levels.levels import Levels
from game.player import Rescueboat
from game.util import imagePath


class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, GAME_HEIGHT)
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

        self.levels = Levels()
        self.setupSprites()

    def setupSprites(self):
        self.player = Rescueboat(imagePath('boat.png'), 2)
        self.boats = arcade.SpriteList()
        self.boats.append(self.player)

        self.player.obstacles = self.levels.logs
        self.player.home = self.levels.home
        self.player.center_x = self.levels.homePos[0]
        self.player.center_y = self.levels.homePos[1]

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
        self.levels.draw()

        drawHome(self.player.passenger)
        self.boats.draw()
        self.drawStatus()

    def drawStatus(self):

        arcade.draw_rectangle_filled(GAME_WIDTH + HALF_STATUS_AREA,
                                     HALF_GAME_HEIGHT, WINDOW_WIDTH - GAME_WIDTH,
                                     GAME_HEIGHT, arcade.color.YELLOW)
        arcade.draw_text("Score : " + str(self.player.score),
                         GAME_WIDTH + STATUS_MARGIN, 350, arcade.color.BLACK_BEAN, 10)

    def update(self, x):
        rescues = arcade.check_for_collision_with_list(self.player, self.levels.pickups)
        if len(rescues) > 0:
            for rescue in rescues:
                rescue.kill()
                self.player.score += 100
                self.player.passenger = True
        if len(self.levels.pickups) == 0 and self.player.passenger == False:
            self.levels.addSurvivor()
        self.levels.update()
        self.boats.update()
