bug, back = None, None
bugX, bugY = 100, 100


def setup():
    global bug, back
    size(600, 500)
    back = loadImage("back.png")
    bug = loadImage("bug.png")
    
        
def draw():
    image(back, 0, 0, 600, 500)
    image(bug, bugX, bugY, 100, 100)
