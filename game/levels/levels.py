import arcade

from game.util import imagePath


class Levels(object):
    def __init__(self):
        self.setupSprites()

    def setupSprites(self):
        self.logs = arcade.SpriteList()
        log = arcade.Sprite(imagePath('log.png'), 2)
        log.center_x = 400
        log.center_y = 400
        self.logs.append(log)

    def update(self):
        pass

    def draw(self):
        self.logs.draw()
