# ゴールキーパー
遠くから近づいてくるボールを弾き返すシンプルな2Dゲーム
ボールのサイズを変化させることでボールが近づいてくる演出をする

# 問題
画像の表示と移動、キーイベントの処理、衝突判定を実装していく
座標の管理にPVectorクラスを使用し、xとyの値を同時に管理する
```
Q1
ウィンドウサイズ：(800, 500)
3つの画像を以下のサイズで表示せよ
背景画像：(800, 500)
ボール：(100, 100)
グローブ：(100, 150)

```
[Ans1](./answer1.pyde)
```
Q2
1. マウスの座標が画像の中心の座標になるように調整して、
マウスに合わせてグローブの画像を移動させよ

2. グローブの画像は、通常は半透明、マウスを押している間だけ普通に描画する
透明度は画像を描画する前にtint関数を呼び出すことで設定する

○tint関数
tint(v,alpha)：画像の塗りつぶし色を設定する
v：色(rgbのように個別指定も可能)
alpha：透明度(0~255)

alpha = 128
if mousePressed:
    alpha = 255
tint(255, alpha)
```
[Ans2](./answer2.pyde)
```
Q3
ボールを向かって飛んでくるように動かす
近づいてくるニュアンスを出すために、徐々にボールの描画サイズを大きくしていき、
ある程度近づいたら、また遠くのランダムな場所にボールを配置する

1. ボールの座標と移動量の管理
pos = PVector(xの初期位置, yの初期位置)
move = PVector(x方向の移動量, y方向の移動量)

2. ボールは画面中央からスタートし、上下左右ランダムな方向へ移動する
- 移動量は-5~5の乱数とする
pos.x = width/2
pos.y = height/2
move.x = random(-5, 5)
move.y = random(-5, 5)

3. ボールの移動量やサイズの計算
frameCount変数を使用し、15で割った余りをローカル変数として使用する
count変数が14になった時に、変数pos,moveを新しい値に設定し、ボールをランダムな位置に戻す

ボールのサイズsはcountの10倍とする
count = frameCount % 15
s = count * 10

ボールは近づくほど移動量が大きく見える
pos.x = pos.x + move.x * count
pos.y = pos.y + move.y * count

```
[Ans3](./answer3.pyde)
```
Q4
衝突判定
以下の条件を満たした時に、手でボールを防いだこととする
if count > 10 and 
    mouseの座標がボールの中にある and
    マウスが押されている:
    防いだ時の処理(スコアの加算、ボールを別の向きに変える)
```
[Ans4](./answer4.pyde)
