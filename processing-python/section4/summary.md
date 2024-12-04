# 関数
```
triangle(x1,y1,x2,y2,x3,y3)
```
## 関数の定義と呼び出し

```python

size(400,400)

def drawHouse(): #関数の定義
    fill(255, 0, 0)
    triangle(200, 50, 100, 150, 300, 150)
    fill(255)
    rect(125, 150, 150, 150)
    fill(30, 200, 200)
    rect(150, 180, 50, 50)

drawHouse()　#関数の呼び出し
```

## 関数の引数

```python

size(600,400)

def drawHouse(x,y): #関数の引数
    fill(255, 0, 0)
    triangle(x, y, x-100, y+50, x+100, y+50)
    fill(255)
    rect(x-75, y+50, 150, 150)
    fill(30, 200, 200)
    rect(x-50, y+80, 50, 50)

drawHouse(100, 100) #関数の呼び出し
drawHouse(300, 100)
drawHouse(500, 100)

```
## 関数の戻り値
```python

def dollarToYen(d, r):
    p = d * r
    return p #関数の戻り値

size(600,400)
textSize(50)
rate = 150

text("$3=", 50, 50)
yen = dollarToYen(3, rate)
text(yen, 150, 50)

text("$7=", 50, 100)
yen = dollarToYen(7, rate)
text(yen, 150, 100)

```

# 問題
```
Q1
setup関数,draw関数を使用して、おでんを描画せよ
```
[Ans1](./answer1.py)

```
Q2
棒の先端がマウスの位置になるように、おでんが移動するようにせよ
```
[Ans2](./answer2.py)
```
Q3
背景を黒にして、おでんのおでんのネタごとに色を変えよ
さらにマウスの場所によって色が変化するようにせよ
```
[Ans3](./answer3.py)
```
Q4
おでんを描くdrawOden函数を作成し、draw関数から呼び出す
+α 作成した関数から複数のおでんを呼び出す
```
[Ans4](./answer4.py)
