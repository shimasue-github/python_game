#モジュール
import tkinter

#結果配列
KEKKA = [
    "あなたはねずみでした。",
    "あなたはうんぱーるーぱ-でした。",
    "あなたはみにおんでした。",
    "あなたは猫でした。",
    "あなたは虎でした。"
]

#クリック時
def click_btn():
    pts =  0
    for i in range(5):
        if bvar[i].get() == True:
            pts =pts +1
        nekodo = int(100*pts/5)
        text.delete("1.0",tkinter.END) #文字列がない状態にする
        text.insert("1.0", "【診断結果】あなたのねこ度は" + str(nekodo)+"%です" + KEKKA[pts]) #文字列を挿入する

#ボード設定
root = tkinter.Tk() #ウィンドウオブジェクト作成
root.title("ねこ診断")
root.resizable(False,False)

#キャンバス
canvas = tkinter.Canvas(root,width=400,height=420,bg="white")
canvas.pack()

#画像
gazou1 = tkinter.PhotoImage(file="1.png")
canvas.create_image(50,168,image=gazou1)
gazou2 = tkinter.PhotoImage(file="2.png")
canvas.create_image(50,212,image=gazou2)
gazou3 = tkinter.PhotoImage(file="3.png")
canvas.create_image(50,257,image=gazou3)
gazou4 = tkinter.PhotoImage(file="4.png")
canvas.create_image(50,297,image=gazou4)
gazou5 = tkinter.PhotoImage(file="5.png")
canvas.create_image(50,337,image=gazou5)

#ボタン
button = tkinter.Button(text="スタート",bg="red",command=click_btn)
button.place(x=100,y=370)

#テキスト
text = tkinter.Text(width=40,height=5)
text.place(x=50,y=30)

#チェックリスト
bvar = [None]*5 #[None]はpython何の存在しない
cbtn = [None]*5
ITEM = [
    "高いところが好き",
    "ボールを見たら転がしたくなる",
    "びっくりすると髪の毛が逆立つ",
    "夜元気になる",
    "匂いに敏感"]
for i in range(5):
    bvar[i] = tkinter.BooleanVar() #オブジェクトを作るためのリスト
    bvar[i].set(False) #チェックをない状態にする
    cbtn[i] = tkinter.Checkbutton(text=ITEM[i],variable=bvar[i]) #リスト
    cbtn[i].place(x=80,y=160+40*i) #ボタンの配置

root.mainloop() #ウィンドウ表示