# リスト
```python
# リストの定義
変数名 = [要素1, 要素2,...]
scores = [75, 87, 96]

# 要素へのアクセス
変数名[インデックス]
※添え字(インデックス)は0から始まる
score[0]
-> 75
```

```python
# 変数を使ったパターン
english = 75
science = 87
math = 96
total = english + science + math

# リストを使ったパターン
scores = [75, 87, 96]
total2 = 0
for i in range(3):
    total2 += scores[i]

print("total={0} total={1}".format(total1, total2))
```

# 画像のリスト
```python
# リストに画像を格納する

# 空の要素の初期化
img = [None, None, None]
index = 0


def setup():
    size(200, 200)
    img[0] = loadImage("close.png")
    img[1] = loadImage("empty.png")
    img[2] = loadImage("lucky.png")


def draw():
    background(200)
    image(img[index], 0, 0)

# クリックするごとに変数indexの値が0→1→2→0...と変化する
def mousepressed():
    global index
    index = index + 1
    if index > 2:
        index = 0
```

# 問題
```
Q1 
for文を使って、画像中央に宝箱を6つ並べて表示せよ
1. 画像のファイルをスケッチのファイルのdataフォルダ内に格納
2. グローバル変数で画像を保持する変数を宣言
3. setup関数の中でloadImage関数を使って画像ファイルを読み込み、変数に格納
4. draw関数の中でimage関数を使って画像を描画
```
[Ans1](./answer1.pyde)
```
Q2
それぞれの状態の画像を変数に格納し、クリックされたら空の箱を表示する
1. リストの宣言と初期化は以下のように実施する
boxes = [None, None, None, None, None, None]
2. for文を使って"unopen"を配置する
3. mousepressed関数を使って、クリックを検出する
- マウスのX座標は0~100の間とする
```
[Ans2](./answer2.pyde)
```
Q3
それぞれの状態の画像を変数に格納し、クリックされたら空の箱を表示する
1. リストの宣言と初期化は以下のように実施する
boxes = [None, None, None, None, None, None]
2. for文を使って"unopen"を配置する
3. mousepressed関数を使って、クリックを検出する
- マウスのX座標は0~100の間とする
```
[Ans3](./answer3.pyde)

