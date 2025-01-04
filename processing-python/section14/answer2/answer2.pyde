kuji = None
img0, img1, img2, img3, img4, img5, img6 \
= None, None, None, None, None, None, None


def setup():
    global kuji, img0, img1, im2, img3, img4, img5, img6
    size(180,400)
    kuji = loadImage("title.png")
    img0 = loadImage("omikuji0.png")
    img1 = loadImage("omikuji1.png")
    img2 = loadImage("omikuji2.png")
    img3 = loadImage("omikuji3.png")
    img4 = loadImage("omikuji4.png")
    img5 = loadImage("omikuji5.png")
    img6 = loadImage("omikuji6.png")
    


def draw():
    image(kuji, 0, 0, 180, 400)


def mousePressed():
    global kuji
    r = int(random(7))
    if r == 0:
        kuji = img0
    if r == 1:
        kuji = img1
    if r == 2:
        kuji = img2
    if r == 3:
        kuji = img3
    if r == 4:
        kuji = img4
    if r == 5:
        kuji = img
    if r == 6:
        kuji = img6
        
