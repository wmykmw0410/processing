beach, sealand, helicopter = None, None, None
x, y = 200, 200
sx, sy = 0, 0

def setup():
    global beach, sealand, helicopter 
    size(900, 500)
    beach = loadImage("beach.jpg")
    sealand = loadImage("sealand.png")
    helicopter = loadImage("helicopter.png")

def draw():
    global x, y, sx, sy
    image(beach, 0,0)
    image(sealand, 600, 300)
    image(helicopter, x, y)
    if keyPressed:
        if keyCode == UP:
            sy -= 5
        elif keyCode == DOWN:
            sy += 5
        elif keyCode == LEFT:
            sx -= 5
        elif keyCode == RIGHT:
            sx += 5
    sx *= 0.98
    sy *= 0.98
    x += sx
    y += sy
    
