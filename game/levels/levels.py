import arcade

from game.items.survivor import Survivor
from game.util import imagePath, RND

from game.items.log import Log


class Levels(object):
    def __init__(self):
        self.setupSprites()
        self.setupHome()

    def setupSprites(self):
        self.logs = arcade.SpriteList()
        self.pickups = arcade.SpriteList()
        self.locations = arcade.SpriteList()
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

    def createCrate(self, x, y, scale):
        log = Log(imagePath('crate.png'), scale)
        log.center_x = x
        log.center_y = y
        self.logs.append(log)

    def createGirder(self, x, y, scale):
        log = Log(imagePath('girder.png'), scale)
        log.center_x = x
        log.center_y = y
        log.wobble = False
        self.logs.append(log)

    def update(self):
        self.logs.update()
        self.pickups.update()

    def draw(self):
        self.logs.draw()
        self.pickups.draw()
