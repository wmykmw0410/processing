# 速度と加速度
```
以下の2つの変数を使用
・座標：画面上の場所(x軸方向の値、y軸方向の値)
・速度：1フレームで移動する量(x軸方向移動量、y軸方向移動量)
```
## 例1 十字キーで円をスムーズに移動させる
```python
x, y = 250, 250 # 座標
sx, sy = 0, 0 # 速度

def setup():
    size(500, 500)

def draw():
    global x, y, sx, sy
    background(200)
    # 加速度
    x += sx　
    y += sy
    ellipse(x, y, 30, 30)
    if keyPressed:    
        if keyCode == UP:
            sy -= 0.1
        elif keyCode == DOWN:
            sy += 0.1
        elif keyCode == LEFT:
            sx -= 0.1
        elif keyCode == RIGHT:
            sx += 0.1
```
# return命令による関数の中断
```python
# 引数で受け取った値を1.1倍して返す関数calc_tax
def calc_tax(price):
    p = price * 1.1
    return p
```
# 例2
```
return命令は必ずしも戻り値を必要としない
単にreturnを実行すると、関数の残りの処理を実施せずに、呼び出し元に制御を戻す
```
```python
x = 0
def setup():
    size(500, 200)
    textSize(50)

def draw():
    global x
    background(200)
    ellipse(x, 130, 50, 50)

    if mousePressed:
        text("PAUSE", 190, 100)
        return
    
    x += 2
    if x > 500:
        x = 0
```
```
draw関数は一定間隔で繰り返し呼び出される
通常は最後まで処理が行われるが、マウスが押下されるとmousePressed変数がTrueとなり、
if文の条件が成立し、return命令が実行され、関数の残りの処理が実行されなくなる
これにより円が移動しなくなる
```
```python
# ゲームオーバーの処理
# 処理が停止しているように見えるが、draw関数は常に定期的に呼び出されている
def draw():
    global gameOver
    ...
    if gameOver:
        <ゲームオーバーの処理>
        return
    ...
    <通常時の処理>
```
# 問題
```
Q1 キャラクターの描画
ウィンドウサイズは(w,h)=(900,500)
以下の3つの画像を表示せよ
beach.jpg：(x,y)=(0,0)
sealand.png：(x,y)=(600,300)
helicopter.png：(x,y)=(200,200)
```
[Ans1](./answer1.pyde)

```
Q2　コントローラー
十字キーでヘリコプターを移動させよ
draw関数の中でkeyPressed変数を使用すること
```
[Ans2](./answer2.pyde)


```
Q3 加速度の追加
sx ：　x軸方向のスピード
sy ：　y軸方向のスピード
x座標とy座標の値はスピードの値を加えることで変化する
x += sx
y += sy
しかし、上記のみではスピードが出過ぎてしまう
よって、スピードが一定の割合で減少するように下記をdraw関数に追加する
sx *= 0.98
sy *= 0.98
```
[Ans3](./answer3.pyde)

```
Q4　ゲームオーバー設定
重力の追加：draw関数に下記を追加する
sy += 0.1

画面の外に出た時にゲームオーバーを表示する
① gameOverというグローバル変数を追加する
②　範囲外に出た時にgameOverをTrueにする
③　draw関数内でgameOverがTrueであれば画面上にメッセージを表示し、以降の処理を行わないreturn命令を実行する

```
[Ans4](./answer4.pyde)
```
Q5ゲームクリア設定
① 着地地点の範囲に入ったらゲームクリアを表示する
着地地点：720 < x < 760, 340 < y < 370
② ゲーム開始からカウントダウンゲージ(fuel)を画面上部に表示する
③ ゲージが0になったらゲームオーバーとする
④ 着陸時のsyが小さいほどスコアが高くなる
⑤ 残り時間が大きいほどスコアが高くなる

```
[Ans5](./answer5.pyde)
