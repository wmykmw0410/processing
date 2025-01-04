unopen = None


def setup():
    global unopen
    size(600, 200)
    unopen = loadImage("close.png")
    
# 画像を6つ並べる
def draw():
    for i in range(6):
        image(unopen, i*100, 50, 100, 100)
        
