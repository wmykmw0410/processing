beach, sealand, helicopter = None, None, None
x, y = 200, 200

def setup():
    global beach, sealand, helicopter 
    size(900, 500)
    beach = loadImage("beach.jpg")
    sealand = loadImage("sealand.png")
    helicopter = loadImage("helicopter.png")

def draw():
    global x, y
    image(beach, 0,0)
    image(sealand, 600, 300)
    image(helicopter, 200, 200)
    if keyPressed:
        if keyCode == UP:
            y -= 10
        elif keyCode == DOWN:
            y += 10
        elif keyCode == LEFT:
            x -= 10
        elif keyCode == RIGHT:
            x += 10
    
    
    
