#モジュール
import tkinter
import random

#変数宣言
index = 0            #ゲーム進行管理する
timer = 0            #時間を管理する
score = 0            #スコア管理する
hisc = 0             #ハイスコアを保持する
difficulty = 0       #難易度の値を入れる
tsugi = 0            #次をセット末う
cursor_x = 0         #カーソル横方向の位置
cursor_y = 0         #カーソル縦方向の位置
mouse_x = 0          #マウスポインタX座標
mouse_y = 0          #マウスポインタY座標
mouse_c = 0          #マウスをクリックした時の変数(フラグ)

#マウスを動かした時の関数
def mouse_move(e):
    global mouse_x, mouse_y   #グローバル変数宣言
    mouse_x = e.x
    mouse_y = e.y
#マウスをクリックした時の関数
def mouse_press(e):
    global mouse_c            #グローバル変数宣言
    mouse_c = 1               #クリックした時に1を代入

neko = []
check = []
for i in range(10):
    neko.append([0, 0, 0, 0, 0, 0, 0, 0])
    check.append([0, 0, 0, 0, 0, 0, 0, 0])

def draw_neko():
    cvs.delete("NEKO")
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x*72+60, y*72+60, image=img_neko[neko[y][x]], tag="NEKO")

def check_neko():
    for y in range(10):
        for x in range(8):
            check[y][x] = neko[y][x]

    for y in range(1, 9):
        for x in range(8):
            if check[y][x] > 0:
                if check[y-1][x] == check[y][x] and check[y+1][x] == check[y][x]:
                    neko[y-1][x] = 7
                    neko[y][x] = 7
                    neko[y+1][x] = 7

    for y in range(10):
        for x in range(1, 7):
            if check[y][x] > 0:
                if check[y][x-1] == check[y][x] and check[y][x+1] == check[y][x]:
                    neko[y][x-1] = 7
                    neko[y][x] = 7
                    neko[y][x+1] = 7

    for y in range(1, 9):
        for x in range(1, 7):
            if check[y][x] > 0:
                if check[y-1][x-1] == check[y][x] and check[y+1][x+1] == check[y][x]:
                    neko[y-1][x-1] = 7
                    neko[y][x] = 7
                    neko[y+1][x+1] = 7
                if check[y+1][x-1] == check[y][x] and check[y-1][x+1] == check[y][x]:
                    neko[y+1][x-1] = 7
                    neko[y][x] = 7
                    neko[y-1][x+1] = 7

def sweep_neko():
    num = 0
    for y in range(10):
        for x in range(8):
            if neko[y][x] == 7:
                neko[y][x] = 0
                num = num + 1
    return num

def drop_neko():
    flg = False
    for y in range(8, -1, -1):
        for x in range(8):
            if neko[y][x] != 0 and neko[y+1][x] == 0:
                neko[y+1][x] = neko[y][x]
                neko[y][x] = 0
                flg = True
    return flg

def over_neko():
    for x in range(8):
        if neko[0][x] > 0:
            return True
    return False

def set_neko():
    for x in range(8):
        neko[0][x] = random.randint(0, difficulty)

def draw_txt(txt, x, y, siz, col, tg):
    fnt = ("Times New Roman", siz, "bold")
    cvs.create_text(x+2, y+2, text=txt, fill="black", font=fnt, tag=tg)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)

#ゲームメイン処理
def game_main():
    global index, timer, score, hisc, difficulty, tsugi
    global cursor_x, cursor_y, mouse_c
    if index == 0: # タイトルロゴ
        draw_txt("どろっぷ", 312, 240, 90, "gray", "TITLE")
        cvs.create_rectangle(168, 384, 456, 456, fill="gray", width=0, tag="TITLE")
        draw_txt("Easy", 312, 420, 20, "white", "TITLE")
        cvs.create_rectangle(168, 528, 456, 600, fill="gray", width=0, tag="TITLE")
        draw_txt("Normal", 312, 564, 20, "white", "TITLE")
        cvs.create_rectangle(168, 672, 456, 744,fill="gray", width=0, tag="TITLE")
        draw_txt("Hard", 312, 708, 20, "white", "TITLE")
        index = 1
        mouse_c = 0
    elif index == 1: # タイトル画面 スタート待ち
        difficulty = 0
        if mouse_c == 1:
            if 168 < mouse_x and mouse_x < 456 and 384 < mouse_y and mouse_y < 456:
                difficulty = 4
            if 168 < mouse_x and mouse_x < 456 and 528 < mouse_y and mouse_y < 600:
                difficulty = 5
            if 168 < mouse_x and mouse_x < 456 and 672 < mouse_y and mouse_y < 744:
                difficulty = 6
        if difficulty > 0:
            for y in range(10):
                for x in range(8):
                    neko[y][x] = 0
            mouse_c = 0
            score = 0
            tsugi = 0
            cursor_x = 0
            cursor_y = 0
            set_neko()
            draw_neko()
            cvs.delete("TITLE")
            index = 2
    elif index == 2: # 落下
        if drop_neko() == False:
            index = 3
        draw_neko()
    elif index == 3: # 揃ったか
        check_neko()
        draw_neko()
        index = 4
    elif index == 4: # 揃ったネコがあれば消す
        sc = sweep_neko()
        score = score + sc*difficulty*2
        if score > hisc:
            hisc = score
        if sc > 0:
            index = 2
        else:
            if over_neko() == False:
                tsugi = random.randint(1, difficulty)
                index = 5
            else:
                index = 6
                timer = 0
        draw_neko()
    elif index == 5: # マウス入力を待つ
        if 24 <= mouse_x and mouse_x < 24+72*8 and 24 <= mouse_y and mouse_y < 24+72*10:
            cursor_x = int((mouse_x-24)/72)
            cursor_y = int((mouse_y-24)/72)
            if mouse_c == 1:
                mouse_c = 0
                set_neko()
                neko[cursor_y][cursor_x] = tsugi
                tsugi = 0
                index = 2
        cvs.delete("CURSOR")
        cvs.create_image(cursor_x*72+60, cursor_y*72+60, image=cursor, tag="CURSOR")
        draw_neko()
    elif index == 6: # ゲームオーバー
        timer = timer + 1
        if timer == 1:
            draw_txt("GAME OVER", 312, 348, 60, "red", "OVER")
        if timer == 50:
            cvs.delete("OVER")
            index = 0
    cvs.delete("INFO")
    draw_txt("SCORE "+str(score), 160, 60, 32, "blue", "INFO")
    draw_txt("HISC "+str(hisc), 450, 60, 32, "yellow", "INFO")
    if tsugi > 0:
        cvs.create_image(752, 128, image=img_neko[tsugi], tag="INFO")
    root.after(100, game_main)

#設定
root = tkinter.Tk()
root.title("落ち物パズル")

#実行する関数を指定
root.bind("<Motion>", mouse_move)               #マウス動かした時
root.bind("<ButtonPress>", mouse_press)         #マウスボタンをクリックした時

#キャンバス設定・配置
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

#画像設定
bg = tkinter.PhotoImage(file="bg.png")           #背景
cursor = tkinter.PhotoImage(file="cursor.png")   #カーソル
img_neko = [
    None,
    tkinter.PhotoImage(file="1.png"),            #ドロップ画像
    tkinter.PhotoImage(file="2.png"),            #ドロップ画像
    tkinter.PhotoImage(file="3.png"),            #ドロップ画像
    tkinter.PhotoImage(file="4.png"),            #ドロップ画像
    tkinter.PhotoImage(file="5.png"),            #ドロップ画像
    tkinter.PhotoImage(file="6.png"),            #ドロップ画像
    tkinter.PhotoImage(file="clear.png")         #クリア画像
]

#キャンバス上に背景を描く
cvs.create_image(456, 384, image=bg)

#メイン処理を呼び出す
game_main()

#ウィンドウに表示
root.mainloop()

