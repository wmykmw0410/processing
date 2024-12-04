x, y = 200, 200

def setup():
    size(400, 400)
    noStroke()

def draw():
    global x, y
    fill(0,0,0, 10)
    rect(0, 0, width, height)
    fill(255)
    ellipse(x, y, 40, 40)

def keyPressed():
    global x, y
    if keyCode == UP:
        y -= 10
    elif keyCode == DOWN:
        y += 10
    elif keyCode == LEFT:
        x -= 10
    elif keyCode == RIGHT:
        x += 10