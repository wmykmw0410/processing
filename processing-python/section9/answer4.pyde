
def setup():
    size(500, 500)
    textSize(40)
    textAlign(CENTER)

def draw():
    r = mouseX /2
    g = mouseY /2
    b = (mouseX + mouseY) /2
    background(r, g, b)
    fill(255)
    rect(0, 450, 500, 50)
    info = "R={0} G={1} B={2}".format(r, g, b)
    fill(0)
    text(info, 250, 485)
