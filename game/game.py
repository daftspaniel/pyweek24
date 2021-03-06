from game.common.constants import *

from game.common.util import imagePath, RND
from game.draw.location import *
from game.items.player import Rescueboat
from game.levels.levels import Levels


class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, GAME_HEIGHT)

        self.state = "Title"
        self.newGame()

    def newGame(self):
        self.levels = Levels()
        self.setupSprites()

    def setupSprites(self):
        self.player = Rescueboat(imagePath('boat.png'), imagePath('person.png'), 1)
        self.boats = arcade.SpriteList()
        self.boats.append(self.player)

        self.player.obstacles = self.levels.logs
        self.player.home = self.levels.home
        self.setPlayerHome()

    def setPlayerHome(self):
        self.player.center_x = self.levels.homePos[0]
        self.player.center_y = self.levels.homePos[1]
        self.player.reset()

    def on_key_press(self, symbol, modifiers):
        if self.state != "Gameplay": return

        if symbol == arcade.key.A:
            self.player.change_angle = 3
        elif symbol == arcade.key.D:
            self.player.change_angle = -3
        elif symbol == arcade.key.W:
            self.player.thrust = 0.15
        elif symbol == arcade.key.S:
            self.player.thrust = -.2
        elif symbol == arcade.key.H:
            self.setPlayerHome()
        elif symbol == arcade.key.J:
            if RND(2) == 1:
                self.player.center_x += 3 + RND(3)
            else:
                self.player.center_y += 3 + RND(3)

    def on_key_release(self, symbol, modifiers):

        if self.state == "GameOver":
            if symbol == arcade.key.SPACE:
                arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
                self.state = "Title"
            return
        if self.state == "Title":
            if symbol == arcade.key.SPACE:
                arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
                self.state = "Gameplay"
                self.newGame()
            return

        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.player.change_angle = 0
        elif symbol == arcade.key.W or symbol == arcade.key.S:
            self.player.thrust = 0

    def on_draw(self):
        if self.state == "Gameplay":
            arcade.start_render()

            self.player.drawTrail()
            self.levels.draw()

            drawHome(self.player.passenger)

            self.boats.draw()
            self.boats[0].drawPassenger()
            self.levels.drawUpper()

            self.drawStatus()
        if self.state == "GameOver":
            drawGameOver()
        if self.state == "Title":
            drawTitleScreen()

    def drawStatus(self):

        arcade.draw_rectangle_filled(GAME_WIDTH + HALF_STATUS_AREA,
                                     HALF_GAME_HEIGHT, WINDOW_WIDTH - GAME_WIDTH,
                                     GAME_HEIGHT, arcade.color.YELLOW)
        TEXT_MARGIN = GAME_WIDTH + STATUS_MARGIN
        arcade.draw_text("Score : " + str(self.player.score),
                         TEXT_MARGIN, 350, arcade.color.BLACK_BEAN, 10)
        arcade.draw_text("Boats : " + str(self.player.boats),
                         TEXT_MARGIN, 380, arcade.color.BLACK_BEAN, 10)

    def update(self, x):

        self.checkSharks()
        self.checkMines()
        self.checkForRescues()

        self.addMoreSurvivors()

        self.levels.update()
        self.boats.update()

    def addMoreSurvivors(self):
        if len(self.levels.pickups) < 3 and self.player.passenger == False:
            self.levels.addSurvivor()

    def checkForRescues(self):
        if self.player.isBackHome(): return
        rescues = arcade.check_for_collision_with_list(self.player, self.levels.pickups)
        if self.player.passenger == False and len(rescues) > 0:
            for rescue in rescues:
                rescue.kill()
                self.player.score += 100
                self.player.passenger = True

    def checkMines(self):
        mineHits = arcade.check_for_collision_with_list(self.player, self.levels.mines)
        for mine in mineHits:
            mine.kill()
            self.player.handleDeadlyCollision()
            self.setPlayerHome()
            if self.player.boats < 0: self.state = "GameOver"

    def checkSharks(self):
        for shark in self.levels.sharks:
            kills = arcade.check_for_collision_with_list(shark, self.levels.pickups)
            for kill in kills:
                kill.kill()
            if not self.player.isBackHome() and arcade.check_for_collision(self.player, shark):
                self.player.handleDeadlyCollision()
                self.setPlayerHome()
                if self.player.boats < 0: self.state = "GameOver"
