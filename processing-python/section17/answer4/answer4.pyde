apple, back, cart = None, None, None
appleX, appleY = 100, 100
speed, score = 3, 0
gameOver = False


def setup():
    global apple, back, cart
    size(500, 500)
    apple = loadImage("apple.png")
    back = loadImage("apple_back.png")
    cart = loadImage("cart.png")
    textAlign(CENTER)
    textSize(32)
    fill(0, 0, 255)


def draw():
    global appleX, appleY, speed, score, gameOver
    cartX = mouseX
    appleY += speed
    
    if 400 < appleY+apple.height and appleY < height \
    and cartX < appleX+apple.width and appleX < cartX+cart.width:    
        appleX = random(width-apple.width)
        appleY = 0
        speed += 1
        score += 1    
            
    if appleY > height:
        gameOver = True   
             
    image(back, 0, 0)
    image(cart, cartX, 400)
    image(apple, appleX, appleY)
    
    text("Score:" + str(score), 200, 50)
    if gameOver:
        text("GAME OVER", width/2, 300)
    
