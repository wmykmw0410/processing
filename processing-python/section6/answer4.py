def setup():
    size(600,600)
   

def draw():
    background(0)
    for x in range(20):
        for y in range(20):
            stroke(mouseX/2, mouseY/2, mouseX+mouseY)
            line(x*30, y*30, mouseX, mouseY)