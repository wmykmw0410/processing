kuji = None


def setup():
    global kuji
    size(180,400)
    kuji = loadImage("title.png")


def draw():
    image(kuji, 0, 0, 180, 400)
