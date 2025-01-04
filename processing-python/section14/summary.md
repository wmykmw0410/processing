# おみくじ
リストと乱数を使ったゲーム  
高速でおみくじ画像が切り替わり、クリックすると切り替わりが停止し、くじが選ばれる

## 複数画像の読み込み
複数の画像のファイル名に規則性がある場合、for文とリストを使って効率的に画像を読み込むことができる
```python
images = [None, None, None, None, None, None, None]
index = 0


def setup():
    size(180, 400)
    
    # 画像の読み込み
    for i in range(7):
        images[i] = loadImage("omikuji" + str(i) + ".png")


def draw():
    background(200)
    image(images[index], 0, 0)


# クリック判定
def mousePressed():
    global index
    index += 1
    if index > 6:
        index = 0

```
# 問題
```
Q1 
画面中央におみくじ画像を表示せよ
ウィンドウサイズ：(180, 400)
最初の画像：title.png
```
[Ans1](./answer1.pyde)
```
Q2 
リストを使用せずにクリックしたらおみくじの結果をランダムに表示せよ
※ 行を途中で折り返す場合は¥もしくは\を使用する
```
[Ans2](./answer2.pyde)
```
Q3 
リストを使用してクリックしたらおみくじの結果をランダムに表示せよ
・くじの結果画像をimagesというリストで管理する
images = [None, None, None, None, None, None, None]

・for文を使って画像をロードし、リストimagesに格納する
```
[Ans3](./answer3.pyde)
```
Q4
以下のグローバル変数を使用して、
おみくじが連続で入れ替わっている時にクリックしたら止まるようにする
```
[Ans4](./answer4.pyde)