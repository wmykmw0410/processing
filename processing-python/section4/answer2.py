def setup():
    size(600, 600)

def draw():
    x = mouseX
    y = mouseY
    background(255)
    line(x, y, x, y+400)
    triangle(x, y+20, x-100, y+100, x+100, y+100)
    ellipse(x, y+170, 100, 100)
    rect(x-100, y+250, 200, 100)