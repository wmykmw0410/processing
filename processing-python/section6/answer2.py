def setup():
    size(600,600)
   

def draw():
    background(200)
    for i in range(20):
        line(i*30, 300, mouseX, mouseY)