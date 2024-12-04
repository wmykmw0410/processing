def setup():
    size(500,500)
    strokeWeight(5)

def draw():
    stroke(mouseX/2, mouseY/2, 255)
    line(pmouseX, pmouseY, mouseX, mouseY)