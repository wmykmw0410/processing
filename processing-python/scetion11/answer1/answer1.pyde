back, ship, fire = None, None, None


def setup():
    global back, ship, fire
    size(600, 600)
    back = loadImage("kasei.jpg")
    ship = loadImage("spaceship.png")
    fire = loadImage("fire.png")
    
    
def draw():
    image(back, 0, 0)
    if keyPressed:
        if keyCode == UP:
            image(fire, 320, 350)
    image(ship, 300, 300)
    
