from tkinter import *

root = Tk()
root.title("GUI")
root. geometry("640x480")

txt = Text(root, width=40, height= 10) # 여러줄 입력 받는거 가능

txt.pack()

txt.insert(END, "plz enter the text")

e = Entry(root, width = 40) # 한줄만 가능
e.pack()
e.insert(0,"enter only one line")
def btncmd():
    print(txt.get("1.0", END)) # 처음부터 끝까지 텍스트 
    # 1.0 에서 1은 1번째 행 0번째 컬럼부터 가져와라~ 이런뜻
    print(e.get())
    txt.delete("1.0", END)
    e.delete(0,END)

btn = Button(root, text = "Click", command = btncmd)
btn.pack()
root.mainloop()