apple, back = None, None
x, y = 0, 0

def setup():
    global apple, back, x, y
    size(500, 500)
    apple = loadImage("apple.png")
    back = loadImage("apple_back.png")
    x = random(width)
    y = 0
    
def draw():
    global x, y
    image(back, 0, 0)
    image(apple, x, y)
    y += 3
    if y > height:
        x = random(width)
        y = 0
