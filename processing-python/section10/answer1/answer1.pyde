beach, sealand, helicopter = None, None, None

def setup():
    global beach, sealand, helicopter 
    size(900, 500)
    beach = loadImage("beach.jpg")
    sealand = loadImage("sealand.png")
    helicopter = loadImage("helicopter.png")

def draw():
    image(beach, 0,0)
    image(sealand, 600, 300)
    image(helicopter, 200, 200)
    
    
