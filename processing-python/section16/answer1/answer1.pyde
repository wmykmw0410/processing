img = None


def setup():
    global img
    size(600, 600)
    img = loadImage("image0.png")
    imageMode(CENTER)


def draw():
    background(255)
    image(img, 300, 300)
    
