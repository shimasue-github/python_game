# オリジナル
import tkinter
import random

def click_btn():
    eat["text"] = random.choice(["激辛","ラーメン","サラダボール","牛タン","お寿司","カフェ","純豆腐","居酒屋"])
    train["text"] = random.choice(["大崎","五反田","目黒","恵比寿","渋谷","原宿","代々木","新宿","目黒","恵比寿","渋谷","原宿","新大久保","高田馬場","目白","池袋","大塚","巣鴨","駒込","田端","恵比寿","西日暮里","日暮里","鶯谷","上野","御徒町","秋葉原","神田","東京","有楽町","新橋","浜松町","田町","高輪","品川"])
    word["text"] = random.choice(["×"])
    eat.update()
    

root = tkinter.Tk()
root.title("きょうのごはん")
root.resizable(False,False)
    
canvas = tkinter.Canvas(root,width=700,height=700,bg="#EBC1C1")
canvas.pack()
character = tkinter.PhotoImage(file = "rice.png")
canvas.create_image(350,300,image=character)
eat = tkinter.Label(root, text="", font=("Times New Roman" ,25),bg="black")
eat.place ( x=370 , y=450)
word= tkinter.Label(root, text="", font=("Times New Roman" ,25),bg="black")
word.place ( x=340 , y=450)
train = tkinter.Label(root, text="", font=("Times New Roman" ,25),bg="black")
train.place ( x=230 , y=450)
button = tkinter.Button(root, text="TAP", font=("Times New Roman" ,20) , background = "gray",foreground = "purple",command=click_btn )
button.place ( x=230 , y=500)
root.mainloop()
