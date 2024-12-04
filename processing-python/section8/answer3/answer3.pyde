apple = None
def setup():
    global apple
    size(400, 400)
    apple = loadImage("apple.png")
    

def draw():
    background(200)
    for x in range(8):
        image(apple, 50*x, 100)
