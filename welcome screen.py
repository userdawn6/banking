import tkinter as tk
from subprocess import call

window = tk.Tk()
window.geometry("350x100")
window.title("welcome to UBA ng")

def click_me():
    call(["python", "banking.py"])

welcome_message_label0 = tk.Label(window, text="WELCOME", font=("Arial", 10))
welcome_message_label0.grid(row=0, column=0, sticky="nsew")

welcome_message_label1 = tk.Label(window, text="TO", font=("Arial", 10))
welcome_message_label1.grid(row=1, column=1, sticky="nsew")

welcome_message_label2 = tk.Label(window, text="UBA NG", font=("Arial", 10))
welcome_message_label2.grid(row=2, column=2, sticky="nsew")

calling = tk.Button(width=15, command=click_me, text="click to continue")
calling.grid(row=4, column=1, sticky="nsew")
calling.config(font=("Arial", 10))
calling.config(fg='#ffffff', bg='#de4343')
window.mainloop()