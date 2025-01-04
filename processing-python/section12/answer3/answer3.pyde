bug, back = None, None
bugX, bugY = 100, 100


def setup():
    global bug, back
    size(600, 500)
    back = loadImage("back.png")
    bug = loadImage("bug.png")
    
        
def draw():
    global bugX, bugY
    
    # 10フレームごとの処理
    if frameCount % 10 == 0:
        bugX = random(0, width)
        bugY = random(0, height)
        
    image(back, 0, 0, 600, 500)
    image(bug, bugX, bugY, 100, 100)
