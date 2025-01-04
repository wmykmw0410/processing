# 衝突判定
## 一定間隔で繰り返し実行する処理

draw関数に記述した処理1秒間に60回(60フレーム)処理される
frameCount変数 -> draw関数が実行されるごとに1増加する
```python
# 100フレームに1回の処理
if frameCount % 100 == 0:
    print(frameCount)
```

## 乱数
random(high) -> 0 ~ high 未満のランダムな数値を生成して返す(float)
random(low, high) -> low ~ high 未満のランダムな数値を生成して返す(float)
```python
# 一定の間隔で向きを変えながら円が移動する

# 円の座標
x, y = 250, 250
# 1フレームで移動する量
dx, dy = 0, 0


def setup():
    size(500, 500)


def draw():
    global x, y, dx, dy
    background(0)

    # 100フレームごとに移動方向が変わる処理
    if frameCount % 100 == 0:
        dx = random(-2, 2)
        dy = random(-2, 2)
    x += dx
    y += dy

    # 円が画面の外に出ないようにする処理
    x = x % width
    y = y % height
    fill(x/2, y/2, 255)
    ellipse(x, y, 50, 50)
```
## int関数
int(num) -> 引数numを整数値にして返す
```python
# 0~5までの乱数
for i in range(10):
    r = random(6)
    dice = int(r)
    print(dice)
```
# 問題
```
Q1 
ウィンドウサイズは(w,h)=(600,500)
背景画像と虫の画像を表示せよ
虫の座標は以下のグローバル変数を使用
bugX, bugY = 100, 100
```
[Ans1](./answer1.pyde)
```
Q2 
フレームごとに虫をランダムな位置へ移動せよ
```
[Ans2](./answer2.pyde)
```
Q3 
ランダムな移動を10フレームごとに修正せよ
if frameCount % 10 == 0:
```
[Ans3](./answer3.pyde)
```
Q4 
虫がクリックされたか判定せよ
クリックされた回数：score
以下の2つの条件を満たしていれば、クリックした座標に虫がいたと判定する
・mouseXの座標がbugX ~ bugX+100の間
・mouseYの座標がbugY ~ bugY+100の間
```
[Ans4](./answer4.pyde)
```
Q5 
虫がスムーズに移動するように以下の3点を実装せよ
・100フレームごとに次の移動地点を乱数で決め、
　移動位置の座標を(nx,ny)という変数に格納する

・1フレームでの移動量を管理するグローバル変数dx,dyの値を以下の計算式で求める
dx = (nx - bugX) / 100
dy = (ny - bugY) / 100

・フレームごとに変数bugXの値を変数dx、変数bugYの値をdyずつ変化させる
```
[Ans5](./answer5.pyde)


