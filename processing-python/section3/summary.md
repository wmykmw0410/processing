# 関数

## setup関数
```
ウィンドウのサイズ設定、画像のロードなど1度だけ必要な処理を記載する
def setup():
    # 最初に1行だけ実行される命令
```

## draw関数
```
プログラムが終了されるまで繰り返し実行する処理を記載する
デフォルトでは1秒間に60回呼び出される
def draw():
    # フレームを描画する度に実行される命令
```

### 例1　　マウスの移動に応じて円を描写し続ける
```python
def setup():
    size(500,500)
    
def draw():
    ellipse(mouseX,mouseY,30,30)
```

### 例2  background関数で背景をクリアし続ける
```python
def setup():
    size(500,500)
    
def draw():
    background(200)
    ellipse(mouseX,mouseY,30,30)
```

## 定義済み変数
```
- mouseX,mouseY  マウスのX,Y座標の値
- pmouseX,pmouseY  1フレーム前のマウスのX,Y座標の値
- width  ウィンドウの幅
- height  ウィンドウの高さ
- frameCount  実行を開始してから何フレーム目かという数値
- mousePressed  マウスが押されている=True,押されていない=False
- keyPressed  キーが押されている=True,押されていない=False
- key  押されているキーの文字列
- keyCode  押されているキーのキーコード
```

### 例3　　frameCount変数
```python
def setup():
    size(500,500)
    textSize(50)

def draw():
    background(200)
    text(frameCount,50,70)
```

### 例4　　mouseX,mouseY変数
```python
def setup():
    size(500,500)
    textSize(50)

def draw():
    background(200)
    textAlign(LEFT)
    text("mouseX =", 50, 50)
    text("mouseY =" ,50, 100)
    textAlign(RIGHT)
    text(mouseX, 350, 50)
    text(mouseY, 350, 100)
    
```
### 例5　　key変数,keyCode変数
[keycode変数](https://learn.microsoft.com/ja-jp/office/vba/language/reference/user-interface-help/keycode-constants)
```python
def setup():
    size(500,500)
    textSize(50)

def draw():
    background(200)
    textAlign(LEFT)
    text("key =", 50, 50)
    text("keyCode =", 50, 100)
    textAlign(RIGHT)
    text(key, 400, 50)
    text(keyCode, 400, 100)
```


# 問題
```
Q1
マウスの軌跡を描画せよ
1フレーム前のマウスの座標と今のマウスの座標をline関数で結ぶ
+α 場所によって線の色が変化するようにする
```
[Ans1](./answer1.py)

```
Q2
マウスの位置から左右と上下に線を、マウスの周囲に2重の円を描画せよ
マウスの位置によって色を変化させること
ウィンドウのサイズが変化してもdraw関数を書き換えなくても済むように、width変数,height変数を使用すること
noFill()：塗り潰しをしない
```
[Ans2](./answer2.py)
