back, ship, fire = None, None, None
pos, speed = None, None


def setup():
    global back, ship, fire, pos, speed
    size(600, 600)
    back = loadImage("kasei.jpg")
    ship = loadImage("spaceship.png")
    fire = loadImage("fire.png")
    pos = PVector(500, 100)
    speed = PVector(0, 1)
    
    
def draw():
    image(back, 0, 0)
    fill(0,255,0)
    if keyPressed:
        if keyCode == UP:
            speed.y -= 0.3
            image(fire, pos.x+20, pos.y+60)
        if keyCode == LEFT:
            speed.x -= 0.1
        if keyCode == RIGHT:
            speed.x += 0.1
    pos.x += speed.x
    pos.y += speed.y 
    speed.y += 0.1
    
    # Speed Gauge
    s = dist(speed.x, speed.y, 0, 0)
    if s > 1:
        fill(255,0,0)
    rect(0, 0, s*100, 30)
    
    image(ship, pos.x, pos.y)
    
