images = [None for i in range(8)]
index = 0


def setup():
    size(600, 600)
    for i in range(8):
        images[i] = loadImage("image" + str(i) + ".png")
    imageMode(CENTER)


def draw():
    background(255)
    image(images[index], 300, 300)


def mousePressed():
    global index
    index = (index + 1) % len(images)


```python
# 別解
def mousePressed():
    global index
    index += 1
    if index > 7:
    index = 0
``` 