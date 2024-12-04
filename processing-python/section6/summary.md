
# ループ
```python
for i in range(ループ回数):
    繰り返し処理
```

## 例1
```python
def setup():
    size(500,250)

def draw():
    line(0, 0, 0, 200)
    line(0, 0, 50, 200)
    line(0, 0, 100, 200)
    line(0, 0, 150, 200)
    line(0, 0, 200, 200)
```

## 例2 for文で繰り返す
```python
def setup():
    size(500,250)

def draw():
    for i in range(10):
        line(0, 0, i*50,200)
```
# 問題
```
Q1
画面中央からマウスの位置まで線を描画せよ
```
[Ans1](./answer1.py)

```
Q2
for文を使ってQ1を複数引くこと
```
[Ans2](./answer2.py)

```
Q3
背景を黒にしてマウスの位置によって色を変える
```
[Ans3](./answer3.py)

```
Q4
更にfor文を使って縦横繰り返す
```
[Ans4](./answer4.py)