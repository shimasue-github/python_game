from tabnanny import check
import tkinter

def click_btn():
    # text = entry.get()
    # button["text"] = text
    text.insert(tkinter.END,"モンスターが現れた！") #最終尾に追加
def check():
    if cval.get() == True:
        print("チェックされています。")
    else :
        print("チェックされていません。")

root = tkinter.Tk()
root.title("練習")
root.geometry("400x200")
# entry = tkinter.Entry(width=20)
# entry.place(x=20,y=20)
cval = tkinter.BooleanVar()
cval.set(True) #true or false チェックの有無
check_button = tkinter.Checkbutton(text="チェックボタン" , variable=umu , command=check)
check_button.pack()
button = tkinter.Button(text="クリック" , command=click_btn)
# button.place(x=20,y=100)
button.pack()
text = tkinter.Text()
text.pack()
root.mainloop()
