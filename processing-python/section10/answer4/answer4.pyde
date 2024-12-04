beach, sealand, helicopter = None, None, None
x, y = 200, 200
sx, sy = 0, 0
gameOver = False

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
    global x, y, sx, sy, gameOver
    image(beach, 0,0)
    image(sealand, 600, 300)
    image(helicopter, x, y)
    
    if gameOver:
        text("GAME OVER", 450, 250)
        return
    
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
    
    if y < 0 or y > 400 or x < 0 or x > 780:
        gameOver = True
    
