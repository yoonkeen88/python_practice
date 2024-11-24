import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title("Menu")
root.geometry("640x480")

def create_new_file():
    print("Create New File")

menu = Menu(root)

# File Menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state = "disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label = "File", menu=menu_file)
# Edit Menu
menu_edit = Menu(menu, tearoff=0)
menu_edit.add_command(label="Edit text")
menu.add_cascade(label = "Edit",menu = menu_edit)

# Language Menu
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label = "python")
menu_lang.add_radiobutton(label = "Java")
menu_lang.add_radiobutton(label = "C++")
menu.add_cascade(label = "Language", menu = menu_lang)

# View menu
menu_view = Menu(menu,tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label = "View", menu=menu_view)

root.config(menu = menu)
root.mainloop()