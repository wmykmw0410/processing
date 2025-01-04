hero = [None, None, None, None]
dir = 0
map = None
x, y = 250, 250


def setup():
    global hero, map
    size(550, 500)
    for i in range(4):
        hero[i] = loadImage("hero" + str(i) + ".png")
    map = loadImage("map.jpg")


def draw():
    global x, y
    background(200)
    image(map, -x, -y)
    image(hero[dir], 250, 250)


def keyPressed():
    global x, y, dir
    if keyCode == UP:
        dir = 0
        y -= 50
    elif keyCode == DOWN:
        dir = 1
        y += 50
    elif keyCode == LEFT:
        dir = 2
        x -= 50
    elif keyCode == RIGHT:
        dir = 3
        x += 50
