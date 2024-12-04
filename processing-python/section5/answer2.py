def setup():
    size(300, 100)
    #noStroke()

def draw():
    background(100)
    fill(255)
    ellipse(50,50,1090,100)
    fill(255)
    ellipse(150,50,100,100)
    fill(255)
    ellipse(250,50,100,100)
    noFill()
    noStroke()
    rect(50, 0, 200, 100)
    stroke(0)
    if mouseX < 100:
    fill(0, 255, 0)
    ellipse(50,50,100,100)
    elif mouseX > 200:
        fill(255, 0, 0)
        ellipse(250,50,100,100)
    else:
        fill(255, 255, 0)
        ellipse(150,50,100,100)