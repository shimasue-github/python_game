#モジュールをインポート
from re import X
import tkinter
import tkinter.messagebox

#変数宣言
key = ""
mx = 1
my = 1
iro = 0

#関数
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ""
    
#リアルタイム処理
def main_proc():
    global mx , my , iro
    
#やり直す場合の処理
    if key == "Shift_L" and iro > 1 :
        canvas.delete("PAINT")
        mx = 1
        my = 1
        iro = 0
        for y in range(7):
            for x in range(10):
                if maze[y][x] == 2:
                    maze[y][x] = 0
                    
    if key == "Up" and maze[my-1][mx] == 0:
        my = my -1
    if key == "Down" and maze[my+1][mx] == 0:
        my = my +1
    if key == "Left" and maze[my][mx-1] == 0:
        mx = mx -1
    if key == "Right" and maze[my][mx+1] == 0:
        mx = mx +1
        
#床を塗っていく
    if maze[my][mx] == 0:
        maze[my][mx] = 2 
        iro = iro + 1
        canvas.create_rectangle(mx*80,my*80,mx*80+79,my*80+79,fill="yellow",width=0 ,tag="PAINT")
        canvas.delete("MYCHR")
        canvas.create_image(mx*80+40,my*80+40,image=img , tag="MYCHR")

#全て塗り終えた場合(アラート)
    if iro == 30:
        canvas.update()
        tkinter.messagebox.showinfo("おめでとう！" ,"全ての床を塗りました！")
    else :
        root.after(100,main_proc)

#設定
root = tkinter.Tk()
root.title("床を全て塗ろう！")

#
root.bind("<KeyPress>" , key_down)
root.bind("<KeyRelease>" , key_up)

#キャンバス作成・設置
canvas = tkinter.Canvas(width=800,height=560,bg="white")
canvas.pack()

#迷路をリストで定義
maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]

#二重ループ [x][y]が壁なら(1)灰色 その他なら(0)白色
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            canvas.create_rectangle( x*80 , y*80 , x*80+80 , y*80+80 , fill="gray")
        else :
            canvas.create_rectangle( x*80 , y*80 , x*80+80 , y*80+80 , fill="white")     
            
#キャラクター
img = tkinter.PhotoImage(file="hito.png")
canvas.create_image(mx*80+40,my*80+40,image=img , tag="MYCHR")

#関数を実行しウィンドウを表示
main_proc()
root.mainloop()

