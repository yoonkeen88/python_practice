from tkinter import *

root = Tk()
root.title("listbox")
root.geometry("640x480")

lbl1 = Label(root, text= "Select your menu\n")
lbl1.pack()

Label(root,text = "\nBurger").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text = "Ham burger", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text = "Cheese burger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text = "Chiken burger", value=3, variable=burger_var)
btn_burger4 = Radiobutton(root, text = "Bull burger", value=4, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()
btn_burger4.pack()

Label(root,text = "\nDrink").pack()

drink_var = IntVar()
btn_drink1 = Radiobutton(root, text = "Coke", value=1, variable=drink_var)
btn_drink2 = Radiobutton(root, text = "Soda", value=2, variable=drink_var)
btn_drink3 = Radiobutton(root, text = "Sprite", value=3, variable=drink_var)
btn_drink4 = Radiobutton(root, text = "Beer", value=4, variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()
btn_drink4.pack()

Label(root,text = "\nSide menu").pack()

side_var = IntVar()
btn_side1 = Radiobutton(root, text = "French fri", value=1, variable=side_var)
btn_side2 = Radiobutton(root, text = "Chiken", value=2, variable=side_var)
btn_side3 = Radiobutton(root, text = "Cheese fri", value=3, variable=side_var)
btn_side4 = Radiobutton(root, text = "Cheese stick", value=4, variable=side_var)

btn_side1.pack()
btn_side2.pack()
btn_side3.pack()
btn_side4.pack()


def btncmd():
  print(f"Selected burger is {burger_var.get()}")
  print(f"Selected drink is {drink_var.get()}")
  print(f"Selected side menu is {side_var.get()}")

btn = Button(root, text="Click",command=btncmd)
btn.pack()

root.mainloop()