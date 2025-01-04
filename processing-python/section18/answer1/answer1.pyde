back, ball, hand = None, None, None


def setup():
    global back, ball, hand
    back = loadImage("keeperview.jpg")
    ball = loadImage("ball.png")
    hand = loadImage("hand.png")
    size(800, 500)


def draw():
    image(back, 0, 0, 800, 500)
    image(ball, 100, 100, 100, 100)
    image(hand, 300, 300, 100, 150)
