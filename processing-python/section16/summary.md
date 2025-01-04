# シルエットクイズ
画像の色味を調整するtint関数を使って画像のシルエット(影)を表現する
リスト内包表記を使って、リストを初期化する

## リスト内包表記
```python
# (例)imagesで6個の画像を管理するリストを作成する
images = [None, None, None, None, None, None]

# リスト内包表記の使用方法
images = [None for i in range(6)]
```

## リスト内包表記の解説
```python
# リストの中身の初期化
images = []

# 複数の要素での初期化
images = [for i in range(6)]

# (例)Noneで初期化
images = [None for i in range(6)]

# (例)for文のループ変数iを使用
numbers = [i*2 for i in range(5)]
-> numbersの中身は[0, 2, 4, 6, 8]となる
```
# 問題
```
Q1
setup関数内でimageMode関数を使用して、画像をウィンドウ中央に表示せよ
ウィンドウサイズ：(600, 600)
画像：image0.png
```
[Ans1](./answer1.pyde)
```
Q2
リスト内包表記を使用して、クリックするたびに次の画像を表示する
```
[Ans2](./answer2.pyde)
```
Q3
最初はシルエット画像を表示し、クリックされたら通常の画像を表示する
さらにクリックされたら次の画像をランダムに表示する

シルエット画像を表示するにはimage関数を呼ぶ前に、画像に色をつける　tint関数を実行する
・tint関数(gray)：画像をグレースクールにする
gray：グレースケール値を0(黒)~255(白)の範囲で指定。
・tint(r,g,b)：画像に色を設定する
```
[Ans3](./answer3.pyde)
