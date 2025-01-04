bug, back = None, None
bugX, bugY = 100, 100
score = 0


def setup():
    global bug, back
    size(600, 500)
    back = loadImage("back.png")
    bug = loadImage("bug.png")
    textSize(40)
    fill(0, 0, 255)
    
        
def draw():
    global bugX, bugY
    
    # 10フレームごとの処理
    if frameCount % 10 == 0:
        bugX = random(0, width)
        bugY = random(0, height)
        
    image(back, 0, 0, 600, 500)
    image(bug, bugX, bugY, 100, 100)
    text("SCORE:" + str(score), 100, 50)
    
    
def mousePressed():
    global score
    if bugX < mouseX < bugX+100 and bugY < mouseY < bugY+100:
        score += 1
        
