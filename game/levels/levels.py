import arcade

from game.common.util import imagePath, RND
from game.items.heli import Heli
from game.items.log import Log
from game.items.shark import Shark
from game.items.survivor import Survivor


class Levels(object):
    def __init__(self):
        self.setupSprites()
        self.setupHome()

    def setupSprites(self):
        self.logs = arcade.SpriteList()
        self.mines = arcade.SpriteList()
        self.sharks = arcade.SpriteList()
        self.pickups = arcade.SpriteList()
        self.locations = arcade.SpriteList()
        self.helecopters = arcade.SpriteList()
        self.rotors = arcade.SpriteList()
        self.buildLevel()

    def buildLevel(self):
        self.createLog(400, 400, 1)
        self.createLog(400, 500, 0.6)
        self.createLog(40, 550, 0.3)
        self.createLog(700, 210, 0.4)
        self.createGirder(200, 410, 9)
        self.createGirder(200, 210, 7)
        self.createCrate(500, 210, 2)
        self.createCrate(20, 410, 3)
        self.createCrate(345, 550, 7)
        self.createShark(444, 444, 1)
        self.createShark(544, 144, 1.1)
        self.createShark(644, 44, 1.2)
        self.addSurvivor()
        self.addSurvivor()
        self.addSurvivor()
        self.addSurvivor()
        self.addChopper()

    def addChopper(self):
        heli = Heli(imagePath('chopper.png'), imagePath('blades.png'), 1)
        heli.center_x = 400
        heli.center_y = -100
        self.helecopters.append(heli)
        self.rotors.append(heli.rotor)

    def addSurvivor(self):
        self.survivor = Survivor(imagePath('person.png'), 0.3)
        self.survivor.center_x = 100 + RND(500)
        self.survivor.center_y = 100 + RND(500)
        self.pickups.append(self.survivor)

    def setupHome(self):
        self.home = arcade.Sprite(imagePath('home.png'), 1)
        self.home.center_x = 50
        self.home.center_y = 100
        self.homePos = (self.home.center_x, self.home.center_y)

    def createLog(self, x, y, scale):
        log = Log(imagePath('log.png'), scale)
        log.center_x = x
        log.center_y = y
        self.logs.append(log)

    def createMine(self, x, y):
        log = Log(imagePath('mine.png'), 1)
        log.center_x = x
        log.center_y = y
        log.turn = False
        self.mines.append(log)

    def createCrate(self, x, y, scale):
        log = Log(imagePath('crate.png'), scale)
        log.center_x = x
        log.center_y = y
        self.logs.append(log)

    def createShark(self, x, y, scale):
        log = Shark(imagePath('shark.png'), scale)
        log.center_x = x
        log.center_y = y
        self.sharks.append(log)

    def createGirder(self, x, y, scale):
        log = Log(imagePath('girder.png'), scale)
        log.center_x = x
        log.center_y = y
        log.wobble = False
        self.logs.append(log)

    def update(self):
        self.logs.update()
        self.pickups.update()
        self.sharks.update()
        self.helecopters.update()
        self.mines.update()
        self.addMines()

    def addMines(self):
        if len(self.mines) > 10: return
        for heli in self.helecopters:
            if 200 < heli.center_y < 550 and RND(200) == 1:
                self.createMine(heli.center_x, heli.center_y)

    def draw(self):
        self.sharks.draw()
        self.logs.draw()
        self.pickups.draw()
        self.mines.draw()

    def drawUpper(self):
        self.helecopters.draw()
        self.rotors.draw()
