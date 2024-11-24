from tkinter import *

root = Tk()
root.title("listbox")
root.geometry("640x480")

chkvar = IntVar() # save the value as a integer in chkvar
checkbox = Checkbutton(root, text = "Never see again only today", variable=chkvar)
# checkbox.select() # 자동 선택 처리
# checkbox.deselect() # 선택 해제 처리
checkbox.pack()

chkvar2 = IntVar() # save the value as a integer in chkvar
checkbox2 = Checkbutton(root, text = "Never see again for a week", variable=chkvar2)
# checkbox.select() # 자동 선택 처리
# checkbox.deselect() # 선택 해제 처리
checkbox2.pack()

def btncmd():
  print(chkvar.get()) # 0: non select, 1: selected
  print(chkvar2.get())
  pass
btn = Button(root, text="Click",command=btncmd)
btn.pack()

root.mainloop()