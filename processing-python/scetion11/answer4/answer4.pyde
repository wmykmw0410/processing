back, ship, fire = None, None, None
pos, speed = None, None
landed, failed = None, None

def setup():
    global back, ship, fire, pos, speed
    size(600, 600)
    back = loadImage("kasei.jpg")
    ship = loadImage("spaceship.png")
    fire = loadImage("fire.png")
    pos = PVector(500, 100)
    speed = PVector(0, 1)
    textSize(40)
    textAlign(CENTER)
    
    
def draw():
    global landed, failed
    image(back, 0, 0)
    fill(0,255,0)
    
    # Game Clear
    if landed:
        text("LANDED!", 300, 300)
        image(ship, pos.x, pos.y, 100, 100)
        return
    
    # Game Over
    if failed:
        text("GAME OVER", 300, 300)
        return

    # Controller
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
    
    # Game clear judgment
    if dist(pos.x, pos.y, 250, 480) < 20 and s < 1:
        landed = True

    # Game over judgment
    if pos.x < 0 or pos.x > 500 or pos.y < 0 or pos.y > 500:
        failed = True
    
    image(ship, pos.x, pos.y)
    
