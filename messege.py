import tkinter
import tkinter.messagebox

def click():
    tkinter.messagebox.showinfo("情報","ボタンを押しました")

root = tkinter.Tk()
root.title("メッセージボックス")
root.geometry("400x200")
btn = tkinter.Button(text="クリック",command=click)
btn.pack()
root.mainloop()