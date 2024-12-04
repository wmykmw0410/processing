apple, orange = None, None
def setup():
    global apple, orange
    size(200, 200)
    apple = loadImage("apple.png")
    orange = loadImage("orange.png")


def draw():
    image(apple, 100, 100)
    image(orange, 50, 50)
