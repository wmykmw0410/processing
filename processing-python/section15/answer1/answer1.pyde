me = None


def setup():
    global me
    size(550, 500)
    me = loadImage("hero1.png")


def draw():
    image(me, 250, 250)
