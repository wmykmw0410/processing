me = None
x, y = 250, 250


def setup():
    global me
    size(550, 500)
    me = loadImage("hero1.png")


def draw():
    background(200)
    image(me, x, y)


def keyPressed():
    global x, y
    if keyCode == UP:
        y -= 50
    elif keyCode == DOWN:
        y += 50
    elif keyCode == LEFT:
        x -= 50
    elif keyCode == RIGHT:
        x += 50
