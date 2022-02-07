from cProfile import label
from distutils.command.config import LANG_EXT
import tkinter

key = ""

def key_down(e):
    global key
    key = e.keysym
    # print("KEY:",str(key))
    
def main_proc():
    label["text"] = key
    root.after(100,main_proc)

root = tkinter.Tk()
root.title("キャラクター")
root.bind("<KeyPress>",key_down)
label = tkinter.Label()
label.pack()
main_proc()
root. mainloop()



