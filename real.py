import tkinter

tmr = 0 #時間をカウントする変数宣言

def count_up():
    global tmr #tmrをグローバル変数として配置
    tmr = tmr + 1 #1ずつ　増やす
    label["text"] = tmr #ラベルに配置
    root.after(1000,count_up) #1秒ごとにこの関数を実行する

root = tkinter.Tk()
root.title("リアルタイム")


canvas = tkinter.Canvas(root , width=500 , height=500)
canvas.pack()
label = tkinter.Label() #ラベルの部品を作り配置
label.pack()
root.after(1000,count_up) #1秒後に指定した関数を呼びだす

root.mainloop()