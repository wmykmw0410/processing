kuji = None
images = [None, None, None, None, None, None, None]


def setup():
    global kuji
    size(180,400)
    kuji = loadImage("title.png")
    for i in range(7):
        images[i] = loadImage("omikuji" + str(i) + ".png")



def draw():
    image(kuji, 0, 0, 180, 400)


def mousePressed():
    global kuji
    r = int(random(7))
    kuji = images[r]
   
