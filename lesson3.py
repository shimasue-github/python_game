#変数の宣言と初期化
a = 100
score = 0
job = "見習い剣士"
#変数の値を変化
print(score)
score = score + 100
print(score)
#変数で文字列を扱う
print(job)
job = "駆け出し剣士"
print(job)
#足し算　+掛け算*
b = job * 2
print(b)
#リスト
enemy = ["魔法使い","スライム","ガイコツ兵"]
print(enemy[0])
print(enemy[1])
print(enemy[2])
#条件分岐
life = 0
if life <= 0 :
    print("ゲームオーバーです。")
if life > 0 :
    print("ゲームを続行します。")
gold = 100 
if gold == 0 :
    print("所持金が0です。")
else :
    print("買い物を続けますか？")
#for文
for i in range(10) :
    print(i)
for i in range(1,5) :
    print(i)
for i in range(10,0,-2) :
    print(i)
#while
i = 0
while i < 5 :
    print(i)
    i = i + 1
#関数
def win():
    print("あなたが勝利しました。")
win()
#引数がある関数
def win(atai):
    print(atai)
    print("あなたが勝利しました。")
win("完封")
#戻り値のある関数
def add(a,b):
    return a+b
c = add (1,2)
print(c)
