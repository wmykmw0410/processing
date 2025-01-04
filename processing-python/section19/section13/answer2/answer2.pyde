unopen, empty, lucky = None, None, None
boxes = [None, None, None, None, None, None]


def setup():
    global unopen, empty, lucky
    size(600, 200)
    unopen = loadImage("close.png")
    empty = loadImage("empty.png")
    lucky = loadImage("lucky.png")
    for i in range(6):
        boxes[i] = unopen


# 画像を6つ並べる
def draw():
    background(200)
    for i in range(6):
        image(boxes[i], i*100, 50, 100, 100)


# クリック判定
def mousePressed():
    for i in range(6):
        if i*100 < mouseX < i*100+100:
            boxes[i] = empty
