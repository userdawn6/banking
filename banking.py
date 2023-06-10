import tkinter
from tkinter import *
from subprocess import call

window = tkinter.Tk()
window.geometry("350x100")
window.title = ("banking ")


def clicked():
    call(["python", "current account.py"])
def clicked2():
    call(["python", "savings account.py"])

Button(master=window, text="current", command=clicked, width=20,height=2 , fg='#ffffff', bg='#de4343').pack()
Button(master=window, text="savings", command=clicked2,width=20,height=2 , fg='#ffffff', bg='#de4343').pack()

window.mainloop()