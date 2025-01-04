images = [None for i in range(8)]
index = 0
show = False


def setup():
    size(600, 600)
    for i in range(8):
        images[i] = loadImage("image" + str(i) + ".png")
    imageMode(CENTER)


def draw():
    background(255)
    if show:
        tint(255)
    else:
        tint(0)
    image(images[index], 300, 300)


def mousePressed():
    global index, show
    if show:
        index = int(random(len(images)))
    show = not show



"""
# 別解
if shiw:
    show = False
else:
    show = True
"""
