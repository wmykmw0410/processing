# 画像の描画

## 画像描画の手順

1. スケッチを保存する
2. スケッチのフォルダの下にdataという名前のフォルダを作成する
3. 画像ファイルをdataフォルダに置く
4. 画像を格納するグローバル変数を宣言する
5. setup関数の中で、loadImage関数を使って画像ファイルを読み込み、④のグローバル変数に代入する
6. draw関数の中で、image関数を使い、位置と大きさを指定して画像を描画する


## 画像描画の関数
```python
・loadImage(filemane)
setup関数の中で実行する
dataフォルダから画像ファイルを読み込み、画像オブジェクトを返す

・image(image, x, y)
画像オブジェクトを画面の座標(x,y)を左上の頂点として描画する
draw関数の中で実行する
画像サイズは元の画像ファイルのサイズが使用される

・image(image, x, y, w, h)
指定したサイズで(幅w,高さh)、画像オブジェクトを画面の座標(x,y)を左上の頂点として描画する
draw関数の中で実行する

・imageMode(mode)
画像表示位置のモードを指定する
mode：CORNER(左上角の座標)、CENTER(画像の中央の座標)、CORNERS(左上と右下を指定)

```

### 例1 画像の描画
```python
fruit = None
def setup():
    global fruit
    size(200, 200)
    fruit = loadImage("apple.png")

def draw():
    image(fruit, 100, 100)
```

# 問題
```
Q1
リンゴとオレンジの画像を好きな場所に描画せよ
```
[Ans1](./answer1/answer1.pyde)

```
Q2
マウスの位置にリンゴを描画せよ
マウスを動かすとリンゴも動くようにすること
その際、マウスが画像の中央になること
```
[Ans2](.//answer2/answer2.pyde)

```
Q3
for文を使って、横一列にリンゴを描画せよ
```
[Ans3](.//answer3/answer3.pyde)

```
Q4
二重forループを使用して、リンゴの画像を一面に描画せよ
```
[Ans4](.//answer4/answer4.pyde)

```
Q5
リンゴが落下するアニメーションを作成せよ
背景にも画像を使用すること
地面まで落下したら、ランダムな場所から再度落下するようにせよ
random(high)：0以上high未満のランダムな値を返す
```
[Ans5](.//answer5/answer5.pyde)
