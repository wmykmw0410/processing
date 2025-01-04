back, ball, hand = None, None, None

# ボールの座標pos
pos = PVector()

# 1フレーム分の移動量move
move = PVector()


def setup():
    global back, ball, hand
    back = loadImage("keeperview.jpg")
    ball = loadImage("ball.png")
    hand = loadImage("hand.png")
    size(800, 500)
    
    # posとmoveの初期化
    pos.x = width/2
    pos.y = height/2
    move.x = random(-5, 5)
    move.y = random(-5, 5)


def draw():
    image(back, 0, 0, 800, 500)
    
    # フレーム数を15で割った余りの0~14までの繰り返しをローカル変数countに代入する
    count = frameCount % 15
    
    # ボールのサイズの変化
    s = count * 10
    if count == 14:
        pos.x = width/2
        pos.y = height/2
        move.x = random(-5, 5)
        move.y = random(-5, 5)
        return
    
    pos.x = pos.x + move.x * count
    pos.y = pos.y + move.y * count
    image(ball, pos.x, pos.y, s, s)

    # ボールの透明度
    alpha = 128
    if mousePressed:
        alpha = 255
    tint(255, alpha)
    image(hand, mouseX-50, mouseY-75, 100, 150)
    tint(255, 255)
