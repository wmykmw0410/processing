x = 300
y = 300
dx = 3

def setup():
    size(600, 600)
    noStroke()

def draw():
    global x, dx
    background(0)
    fill(0, 255, 0)
    x  = x + dx
    if x > 600 or x < 0:
        dx *= -1
    ellipse(x, y, 30, 30)