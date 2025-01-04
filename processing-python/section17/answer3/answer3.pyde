apple, back, cart = None, None, None
appleX, appleY = 100, 100
speed = 3

def setup():
    global apple, back, cart
    size(500, 500)
    apple = loadImage("apple.png")
    back = loadImage("apple_back.png")
    cart = loadImage("cart.png")


def draw():
    global appleX, appleY, speed
    cartX = mouseX
    appleY += speed
    if appleY > height:
        appleX = random(width-apple.width)
        appleY = 0
        speed += 1
    image(back, 0, 0)
    image(cart, cartX, 400)
    image(apple, appleX, appleY)
    
