import tkinter

def click_btn():
    button["text"] = "クリックしました。"

root = tkinter.Tk()
root.title("python練習") 
root.geometry("1200x1200")
label = tkinter.Label(root , text= "ラベルだよ", font =("Times New Roman" , 24))
button = tkinter.Button(root , text= "ボタンだよ", font =("Times New Roman" , 24), command=click_btn)
canvas = tkinter.Canvas(root , width=1200 , height=1200, bg = "skyblue")
character = tkinter.PhotoImage(file="character1.png")
canvas.create_image(500,500,image= character )
label.place(x=100,y=50)
button.place(x=200,y=100)
canvas.pack()
root.mainloop()

