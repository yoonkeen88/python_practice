from tkinter import *

def btncmd():
    print("button has clicked")



root = Tk()
root.title("yoonkeen's gui program")
root.geometry("640x480")

btn1 = Button(root, text = "button1")
btn1.pack()

btn2 = Button(root,padx=5,pady=10, text = "button2") # padx pady 패딩인듯
btn2.pack()

btn3 = Button(root, padx=10,pady=20, text = "button3")
btn3.pack()

btn4 = Button(root, width=10, height = 3, text = "button4") # button의 크기 자체를 설정
btn4.pack()

btn5 = Button(root, fg="red",bg = "yellow", text = "button5")
btn5.pack()

photo = PhotoImage(file="gui_basic/Sign.png")
btn6 = Button(root, width=10, height=10,image=photo, command=btncmd)
btn6.pack()


root.mainloop() # mainloop 를 통해 창이 닫히지 않게 해줌
