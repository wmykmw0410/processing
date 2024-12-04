def setup():
    size(600, 600)
    strokeWeight(5)

def draw():
    background(0)
    drawOden(mouseX, mouseY)


def drawOden(x,y):
    stroke(255)
    line(x, y, x, y+400)
    fill(255, x/2, y/2)
    triangle(x, y+20, x-100, y+100, x+100, y+100)
    fill(x/2, 255, y/2)
    ellipse(x, y+170, 100, 100)
    fill(x/2, y/2, 255)
    rect(x-100, y+250, 200, 100)