import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title("listbox")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode = "indeterminate")
# progressbar2 = ttk.Progressbar(root, maximum=100, mode = "determinate")

# progressbar.start(10)# They move per 10ms # speed adjust
# progressbar.pack()

# progressbar2.start(100)
# progressbar2.pack()

# def btncmd():
#     progressbar.stop()
#     progressbar2.stop()
#     pass

# btn = Button(root, text="Stop",command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root,maximum=100, length=100, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(101):
        time.sleep(0.01) # 0.01sec 
        p_var2.set(i) # set the progressbar value  
        progressbar2.update() # updating the value
        print(p_var2.get())
    pass

btn = Button(root, text="start",command=btncmd2)
btn.pack()
root.mainloop()