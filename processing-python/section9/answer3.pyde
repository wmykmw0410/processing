s = ""

def setup():
    size(600, 100)
    textSize(50)

def draw():
    background(200)
    text(s, 20, 50)

def keyPressed():
    global s
    if key == ENTER:
        s = ""
    else:
        s  += key 
