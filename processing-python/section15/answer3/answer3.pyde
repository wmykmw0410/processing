me, map = None, None
x, y = 250, 250


def setup():
    global me, map
    size(550, 500)
    me = loadImage("hero1.png")
    map = loadImage("map.jpg")


def draw():
    global x, y
    background(200)
    image(map, -x, -y)
    image(me, 250, 250)


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
