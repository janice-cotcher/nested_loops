screen_width = 200


def setup():
    size(screen_width, screen_width)


def onec(pen_enabled, square_size):
    if pen_enabled:
        square_x = 0
        while square_x < screen_width:
            rect(square_x, 0, square_size, square_size)
            square_x = square_x + square_size


def draw():
    onec(True, 100)
