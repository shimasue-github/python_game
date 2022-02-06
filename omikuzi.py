from distutils import command
import tkinter
import random

def click_btn():
    label["text"] = random.choice(["大吉","中吉","小吉","吉"])
    label.update()

root = tkinter.Tk()
root.title("おみくじ")
root.resizable(False,False)
    
canvas = tkinter.Canvas(root,width=1200,height=600,bg="#BEBFA0")
canvas.pack()
character = tkinter.PhotoImage(file = "character1.png")
canvas.create_image(400,300,image=character)
label = tkinter.Label(root, text="??", font=("Times New Roman" ,70))
label.place ( x=680 , y=70)
button = tkinter.Button(root, text="おみくじを引く", font=("Times New Roman" ,60) , command=click_btn ,bg="white")
button.place ( x=680 , y=350)
root.mainloop()