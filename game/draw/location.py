import arcade


def drawHome(altColour):

    if altColour:
        color = arcade.color.BRIGHT_GREEN
    else:
        color = arcade.color.BLANCHED_ALMOND
    arcade.draw_circle_filled(50, 100, 45, color)
    arcade.draw_circle_outline(50, 100, 45, arcade.color.RED, 10)
    arcade.draw_circle_outline(50, 100, 25, arcade.color.RED, 10)
    arcade.draw_circle_outline(50, 100, 5, arcade.color.RED, 2)
