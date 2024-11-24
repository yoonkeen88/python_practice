from tkinter import *
import tkinter.messagebox as msgbox
root = Tk()
root.title("Menu")
root.geometry("640x480")

# Suppose Reservation sys of train

def info():
    response=msgbox.showinfo("Notification","Complete the reservation")

def warn():
    msgbox.showwarning("Warning","Sold out")

def error():
    msgbox.showerror("Error","Bill Error Check the credit card")

def okcancel():
    response=msgbox.askokcancel("OK / Cancel","This seat is with child seat.\nAre you sure?")
    if response == 1:
        print("OK")
    elif response == 0:
        print("Cancel")

def retrycancel():
    response = msgbox.askretrycancel("Retry / Cancel","Are you want retry?")
    if response == 1:
        print("Retry")
    elif response == 0:
        print("Cancel")
def yesno():
    response=msgbox.askyesno("Yes / No","This seat is reverse direction. You want?")
    if response == 1:
        print("Yes")
    elif response == 0:
        print("No")
def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="The change is not saved.\nSave?")
    # yes: Exit after save
    # no: Exit non-save
    # cancel: Cancel exit 
    if response == 1:
        print("yes")
    elif response == 0:
        print("no")
    else: 
        print("cancel")

Button(root, command=info, text = "Notification").pack()
Button(root, command=warn, text = "Warning").pack()
Button(root, command=error, text = "Error").pack()

Button(root, command=okcancel, text = "OK / Cancel").pack()
Button(root, command=retrycancel, text = "Retry / Cancel").pack()
Button(root, command=yesno, text = "Yes / No").pack()
Button(root, command=yesnocancel, text = "Yes / No / Cancel").pack()

root.mainloop()