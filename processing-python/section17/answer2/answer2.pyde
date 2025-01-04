apple, back, cart = None, None, None


def setup():
    global apple, back, cart
    size(500, 500)
    apple = loadImage("apple.png")
    back = loadImage("apple_back.png")
    cart = loadImage("cart.png")


def draw():
    cartX = mouseX
    image(back, 0, 0)
    image(cart, cartX, 400)
    image(apple, 100, 100)
    
