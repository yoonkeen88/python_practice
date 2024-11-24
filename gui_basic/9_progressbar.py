import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("listbox")
root.geometry("640x480")


def btncmd():
    pass

btn = Button(root, text="Select",command=btncmd)
btn.pack()

root.mainloop()