apple, orange = None, None

def setup():
    global apple, orange
    size(200, 200)
    apple = loadImage("apple.png")
    orange = loadImage("orange.png")
    
def draw():
    image(orange, 50, 50)
    image(apple, 100, 100)
