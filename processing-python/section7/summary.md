# 変数のスコープ

## ローカル変数(局所変数)；
関数の中で宣言された変数
その変数の中でしか使えない
関数を実行する度に初期化される

## グローバル変数(広域変数)；
関数の外で宣言された変数
どの関数からも利用できる
プログラム実行中は値が保持される

```python
x,y = 100, 100 #　グローバル変数

def setup():
    size(x*2, y*2)

def draw():
    r = 50　# ローカル変数
    ellipse(x, y, r, r)
```

## グローバル変数の更新
### score変数を更新していくプログラムを考える
### 失敗例1 
```python
score = 0 # グローバル変数

def setup():
    size(300, 100)
    textSize(50)

def draw():
    background(200)
    score = score + 1　# ローカル変数
    text("score:"+str(score), 20, 50)
```

### 失敗例2 
```python

def setup():
    size(300, 100)
    textSize(50)

def draw():
    score = 0 # ローカル変数
    background(200)
    score = score + 1　# ローカル変数
    text("score:"+str(score), 20, 50)
```
### 成功例1
```python
score = 0

def setup():
    size(300, 100)
    textSize(50)

def draw():
    global score # global命令を追加する
    background(200)
    score = score + 1 # ローカル変数
    text("score:"+str(score), 20, 50)
```
# 問題
```
Q1
setup関数とdraw関数を使って黒い背景の画面中央に緑色の円を描画せよ
```
[Ans1](./answer1.py)

```
Q2
円を右方向に移動し、右端からから左端に移動せよ
ボールの座標はグローバル変数x,yを使用すること
```
[Ans2](./answer2.py)

```
Q3
左右の壁で反射するように移動させよ
x軸方向の移動量を保持する変数dxを使用する
```
[Ans3](./answer3.py)

```
Q4
y軸方向にも反射するようにせよ
ウィンドウサイズの変更にも対応できるようにウィンドウの幅をwidth、高さをheightとし、
背景をクリアする処理を下記とする
fill(0, 0, 0, 10) # 4番目の引数は透明度を表す(0~255)
rect(0, 0, width, height)
```
[Ans4](./answer4.py)