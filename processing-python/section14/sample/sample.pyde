images = [None, None, None, None, None, None, None]
index = 0


def setup():
    size(180, 400)
    
    # 画像の読み込み
    for i in range(7):
        images[i] = loadImage("omikuji" + str(i) + ".png")


def draw():
    background(200)
    image(images[index], 0, 0)


# クリック判定
def mousePressed():
    global index
    index += 1
    if index > 6:
        index = 0
