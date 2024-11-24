from tkinter import *

root = Tk()
root.title("Menu")
root.geometry("640x480")
Label(root, text = "Select the menu").pack(side="top")
Button(root, text = "Order").pack(side="bottom")
frame_burger = Frame(root, padx=20,pady=20 ,relief = "solid", bd = 1, border=10) 
# relief = 테두리 bd = border 
frame_burger.pack(side = "left",fill = "both",expand=True)

Button(frame_burger, text = "Ham burger").pack()
Button(frame_burger, text = "Chiken burger").pack()
Button(frame_burger, text = "Cheese burger").pack()
Button(frame_burger, text = "Bull burger").pack()

frame_drink = LabelFrame(root,text = "Drink", padx=20,pady=20 ,relief = "solid", bd = 1, border=10) 
frame_drink.pack(side="right",fill = "both", expand=True) #expand=True 꽉채우기
Button(frame_drink, text="Coke").pack()

Button(frame_drink, text="Sprite").pack()
Button(frame_drink, text="Soda").pack()
Button(frame_drink, text="Beer").pack()

root.mainloop()