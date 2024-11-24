from tkinter import *

def btncmd():
    print("button has clicked")



root = Tk()
root.title("yoonkeen's gui program")
root.geometry("1280x960")

lbl = Label(root, text = "hello")
lbl.pack()

photo  = PhotoImage(file="gui_basic/img/Sign.png")
lbl2 = Label(root,image=photo, width=10,height=10)
lbl2.pack()


def change():
    lbl.config(text = "see you")
    global photo2
    photo2 = PhotoImage(file= "gui_basic/img/x.png")
    
    lbl2.config(image=photo2)

btn = Button(root, text = "click",command=change)
btn.pack()
root.mainloop() # mainloop 를 통해 창이 닫히지 않게 해줌
