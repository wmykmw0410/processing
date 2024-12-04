def setup():
    size(500,500)
    strokeWeight(5)

def draw():
    background(0)
    stroke(mouseX/2, mouseY/2, 255)
    line(mouseX, 0, mouseX, height)
    line(0, mouseY, width, mouseY)
    noFill()
    ellipse(mouseX, mouseY, 30, 30)
    ellipse(mouseX, mouseY, 60, 60)
