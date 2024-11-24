import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("listbox")
root.geometry("640x480")

values = [str(i) + "day" for i in range(1,32)]
combobox = ttk.Combobox(root, height = 5, values = values)
combobox.pack()
combobox.set("Bill day") 

readonly_combobox = ttk.Combobox(root, height = 10, values = values, state="readonly")
readonly_combobox.pack()
readonly_combobox.set("Bill day") 
def btncmd():
    print(f"The credet card bill day is {combobox.get()}")
    print(f"The credet card bill day is {readonly_combobox.get()}")
    pass

btn = Button(root, text="Select",command=btncmd)
btn.pack()

root.mainloop()