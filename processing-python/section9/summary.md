# イベント(マウスの移動やキーの押下による入力)
## イベントハンドラの定義
|イベントハンドラ|内容|  
| ----- | ------ |
|keyPressed()|キーが押されたら|
|keyReleased()|キー離されたら|
|mousePressed()|マウスが押されたら|
|mouseReleased()|マウスが離されたら|
|mouseClicked()|マウスがクリックされたら|
|mouseMoved()|マウスが動いたら|
|mouseDragged()|マウスがドラッグされたら|

## 例1
```python
info = ""
def setup():
    size(600, 100)
    textSize(30)

def draw():
    background(100)
    text(info, 10, 50)

def keyPressed():
    global info
    info = "keyPressed key={0} keyCode={1}".format(key, keyCode)

def keyReleased():
    global info
    info = "keyPressed key={0} keyCode={1}".format(key, keyCode)

def mousePressed():
    global info
    info = "mousePressed x={0} y={1}".format(mouseX, mouseY) 

def mouseReleased():
    global info
    info = "mouseReleased x={0} y={1}".format(mouseX, mouseY) 

def mouseClicked():
    global info
    info = "mouseClicked x={0} y={1}".format(mouseX, mouseY) 

def mouseMoved():
    global info
    info = "mouseMoved x={0} y={1}".format(mouseX, mouseY) 

def mouseDragged():
    global info
    info = "mouseDragged x={0} y={1}".format(mouseX, mouseY) 
```
## 定義済み変数を参照する方法
|変数|内容|  
| ----- | ------ |
|key|直近に押下されたキーの文字(アルファベットや数値など)|
|keyCode|直近に押下されたキーのコード(カーソル,Alt,Ctrl,Shiftなど文字を持たないキーの判定に利用)|
|keyPressed|キーが押下状態か否か|
|mousePressed|マウスが押下状態か否か|

## 例2
```python
def setup():
    size(600, 100)
    textSize(30)

def draw():
    background(100)
    info = "key={0} keyCode{1}" .format(key, keyCode)
    if keyPressed:
        info += "keyPressed"
    if mousePressed:
        info += "mousePressed"
    text(info, 10, 50)
```

## 書式指定文字列
```python
# 文字列と数値を足し算するとエラーになる
a = "hello" + 3
print(a)

# 文字列と数値を連結するにはstr関数を使って文字列を数値に変換する
a = "hello" + str(3)
print(a)

# format命令を使うと、型変換が不要になる
## 文字列中の{番号}：format命令の何番目の引数を埋め込むか
a = 3
b = 5
c = "a={0}, b={1}, a+b={2}".format(a, b, a+b)
print(c)
```

# 問題
```
Q1
十字キーで画面上の円を移動させよ
keyPressed関数を使用してイベント処理せよ
グローバル変数x,yで円の中心座標を管理せよ
また以下のコードで背景をクリアせよ
fill(0,0,0,10)
rect(0, 0, width, height)
```
[Ans1](./answer1.pyde)

```
Q2
keyPressed関数を使わずに十字キーで円を移動させよ
draw関数の中からkeyCode変数やkeyPressed変数を参照すること
```
[Ans2](./answer2.pyde)

```
Q1とQ2の比較
Q1：1回はすぐに反応するが、ワンクッションあってから連続して移動する(キーリピート機能)
Q2：すぐに反応する。移動速度が速い。→リアルタイム・アクション系のゲームで使用される
```

```
Q3
タイプした文字列を画面に表示せよ
Enterキーを押下した時に文字列をクリアすること
```
[Ans3](./answer3.pyde)

```
Q4
マウスの移動に応じて背景色を変化させよ
その色のR,G,B成分の値を画面下に表示させよ
```
[Ans4](./answer4.pyde)
