x, y = 300, 300
dx, dy = 3, 2

def setup():
    size(600, 600)
    noStroke()

def draw():
    global x, y, dx, dy
    fill(0, 0, 0, 10)
    rect(0, 0, width, height)
    x = x + dx
    y = y + dy
    fill(0, 255, 0)
    if x > width or x < 0:
        dx *= -1
    if y > height or y < 0:
        dy *= -1
    ellipse(x, y, 30, 30)