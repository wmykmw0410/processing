def setup():
    size(400,300)
    strokeWeight(5)

def draw():
    if mousePressed:
        line(pmouseX, pmouseY, mouseX, mouseY)