apple = None
def setup():
    global apple
    size(200, 200)
    apple = loadImage("apple.png")
    imageMode(CENTER)

def draw():
    background(200)
    image(apple, mouseX, mouseY)
