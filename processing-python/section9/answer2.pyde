x, y = 200, 200

def setup():
    size(400, 400)
    noStroke()

def draw():
    global x, y
    fill(0,0,0, 10)
    rect(0, 0, width, height)
    if keyPressed:
        if keyCode == UP:
            y -= 10
        elif keyCode == DOWN:
            y += 10
        elif keyCode == LEFT:
            x -= 10
        elif keyCode == RIGHT:
            x += 10
    fill(255)
    ellipse(x, y, 40, 40)

