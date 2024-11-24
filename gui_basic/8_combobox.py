from tkinter import *

root = Tk()
root.title("listbox")
root.geometry("640x480")


def btncmd():
    pass

btn = Button(root, text="Click",command=btncmd)
btn.pack()

root.mainloop()