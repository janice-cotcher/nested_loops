def setup():
    size(150, 100)
    

def draw_red_target(x, y):
    fill(255, 0, 0)
    ellipse(20*x + 20, 20*y + 20, 20, 20)


def draw_blue_target(x, y):
    fill(0, 0, 255)
    ellipse(20*x + 20, 20*y + 20, 20, 20)


def draw():
    background(0)
    for y in range(3):
        for x in range(5):
            if y % 2 == 0:
                draw_blue_target(x, y)
            else:
                draw_red_target(x, y)
