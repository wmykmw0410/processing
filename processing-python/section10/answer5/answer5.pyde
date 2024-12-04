beach, sealand, helicopter = None, None, None
x, y = 200, 200
sx, sy = 0, 0
fuel = 900
gameOver, gameClear = False, False

def setup():
    global beach, sealand, helicopter 
    size(900, 500)
    beach = loadImage("beach.jpg")
    sealand = loadImage("sealand.png")
    helicopter = loadImage("helicopter.png")
    textSize(50)
    textAlign(CENTER)
    fill(0)

def draw():
    global x, y, sx, sy, gameOver, gameClear, fuel
    image(beach, 0,0)
    image(sealand, 600, 300)
    image(helicopter, x, y)
    rect(0, 0, fuel, 30)
    
    if gameOver:
        text("GAME OVER", 450, 250)
        return
    
    if gameClear:
        score = fuel
        score -= int(sy * 10)
        text("CLEAR: SCORE="+str(score), 450, 250)
        return
    
    fuel -= 1
        
    
    if keyPressed:
        if keyCode == UP:
            sy -= 1
        elif keyCode == DOWN:
            sy += 1
        elif keyCode == LEFT:
            sx -= 1
        elif keyCode == RIGHT:
            sx += 1
    sy += 0.1
    sx *= 0.98
    sy *= 0.98
    x += sx
    y += sy
    
    if y < 0 or y > 400 or x < 0 or x > 780 or fuel < 0:
        gameOver = True
        
    if 720 < x < 760 and 340 < y < 370:
        gameClear = True
    
