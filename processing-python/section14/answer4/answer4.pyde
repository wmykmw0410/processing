kuji = None
images = [None, None, None, None, None, None, None]
index = 0
paused = False


def setup():
    size(180, 400)
    for i in range(7):
        images[i] = loadImage("omikuji" + str(i) + ".png")



def draw():
    global index
    if paused:
        return
    index = index + 1
    if index > 6:
        index = 0
    image(images[index], 0, 0, 180, 400)


def mousePressed():
    global paused
    if paused == True:
        paused = False
    else:
        paused = True
   

```
# (別解)0~6までを順番に変化させる方法
index = (idex + 1) % 7

# (別解)マウスがクリックされた時のpaused変数を変化させる方法
def mousePressed():
    global paused
    paused = not paused