fruit = None
def setup():
    global fruit
    size(200, 200)
    fruit = loadImage("apple.png")

def draw():
    image(fruit, 100, 100)
