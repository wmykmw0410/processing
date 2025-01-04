bug, back = None, None
bugX, bugY = 100, 100
dx, dy = 0, 0
score = 0


def setup():
    global bug, back
    size(600, 500)
    back = loadImage("back.png")
    bug = loadImage("bug.png")
    textSize(40)
    fill(0, 0, 255)
    
        
def draw():
    global bugX, bugY, dx, dy
    
    # 100フレームごとの処理
    if frameCount % 100 == 0:
        nx = random(0, width)
        ny = random(0, height)
        
        # 1フレーム分の移動量
        dx = (nx - bugX) / 100
        dy = (ny - bugY) / 100
    bugX += dx
    bugY += dy
        
    image(back, 0, 0, 600, 500)
    image(bug, bugX, bugY, 100, 100)
    text("SCORE:" + str(score), 100, 50)
    
    
def mousePressed():
    global score
    if bugX < mouseX < bugX+100 and bugY < mouseY < bugY+100:
        score += 1
        
