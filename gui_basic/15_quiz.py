from tkinter import *
import os
from tkinter import ttk

filename ="mynote.txt"
def create_new_file():
    pass
def open_file():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file:
            txt.insert(END, file.read())
def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0",END))

root = Tk()
root.title("제목 없음 - windows 메모장")
root.geometry("640x480")
scrollbar = Scrollbar(root)
scrollbar.pack(side = "right", fill="y")
txt = Text(root, yscrollcommand=scrollbar.set) # 여러줄 입력 받는거 가능
txt.pack(side = "left", fill="both", expand=True)




scrollbar.config(command=txt.yview)


## menu byu ttk
menu = Menu(root)

# File Menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...",command=open_file )
menu_file.add_separator()
menu_file.add_command(label="Save All",  command=save_file)
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

root.mainloop() # mainloop 를 통해 창이 닫히지 않게 해줌
