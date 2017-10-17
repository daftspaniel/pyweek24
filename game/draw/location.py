import arcade


def drawHome(altColour):
    if altColour:
        color = arcade.color.BRIGHT_GREEN
    else:
        color = arcade.color.BLANCHED_ALMOND
    arcade.draw_circle_filled(50, 100, 45, color)
    arcade.draw_circle_outline(50, 100, 45, arcade.color.ANDROID_GREEN, 10)
    arcade.draw_circle_outline(50, 100, 25, arcade.color.ANDROID_GREEN, 10)
    arcade.draw_circle_outline(50, 100, 5, arcade.color.ANDROID_GREEN, 2)


def drawGameOver():
    arcade.draw_text("GAME OVER", 250, 380, arcade.color.YELLOW_ORANGE, 60)
    arcade.draw_text("Press Space to Continue", 250, 80, arcade.color.YELLOW_ORANGE, 20)


def drawTitleScreen():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.draw_text("PyWeek24", 250, 380, arcade.color.YELLOW_ORANGE, 60)

