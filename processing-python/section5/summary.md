# 条件分岐
```python
if 条件:
    条件が成立時の処理
elif 条件:
    条件が成立時の処理
else:
    条件が不成立時の処理
```

## 比較演算子

|演算子|意味|  
| ----- | ------ |
| ==|等しい|
|>|より大きい|
|>=|以上|
|<|より小さい|
|<=|以下|

### 例1
```python
def setup():
    size(300,300)

def draw():
    background(200)
    if mouseX < 100:
        ellipse(width/2, height/2, 100, 100)
    elif mouseX < 200:
        rect(width/2-50, height/2-50, 100, 100)
    else:
        triangle(150, 100, 50, 200, 250, 200)
```

## 論理演算子
```
- 条件1 かつ 条件2：条件1 and 条件2
- 条件1 または 条件2：条件1 or 条件2
```

### 例2
```python
def setup():
    size(300,300)

def draw():
    background(200)
    line(0, height/2, width, height/2)
    line(width/2, 0, width/2, height)
    if mouseX < width/2 and mouseY < height/2:
        ellipse(width/2, height/2, 100, 100)
```
### 例3
```python
def setup():
    size(300,300)

def draw():
    background(200)
    line(0, height/2, width, height/2)
    line(width/2, 0, width/2, height)
    if mouseX < width/2 or mouseY < height/2:
        ellipse(width/2, height/2, 100, 100)
```
### 例4  歩行者用信号機
```python
def setup():
    size(120,250)
    strokeWeight(10)
    stroke(255)

def draw():
    background(200)
    if mouseY < height/2:
        fill(200, 0, 0)
        rect(10, 10, 100, 100)
    else:
        fill(0, 200, 0)
        rect(10, 120, 100, 100)

```
# 問題
```
Q1
マウスで線を描画せよ
mousePressed変数：マウス押下時にTrue、そうでない時にFalse
```
[Ans1](./answer1.py)

```
Q2
信号機を作成せよ
マウスが画面左1/3にあるときは青、画面右1/3にあるときは赤、それ以外は黄色を点灯させる
```
[Ans2](./answer2.py)


