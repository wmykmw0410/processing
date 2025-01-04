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

    # ボールの透明度
    alpha = 128
    if mousePressed:
        alpha = 255
    tint(255, alpha)
    image(hand, mouseX-50, mouseY-75, 100, 150)
    tint(255, 255)
