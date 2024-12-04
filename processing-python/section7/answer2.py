x = 300
y = 300

def setup():
    size(600, 600)
    noStroke()

def draw():
    global x
    background(0)
    fill(0, 255, 0)
    x  += 1
    if x > 600:
        x = 0
    ellipse(x, y, 30, 30)