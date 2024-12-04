def setup():
    size(600,600)
   

def draw():
    background(0)
    for i in range(20):
        stroke(mouseX/2, mouseY/2, mouseX+mouseY)
        line(i*30, 300, mouseX, mouseY)