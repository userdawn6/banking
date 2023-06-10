import tkinter as tk
from subprocess import call

def welcome():
    call(["python", "welcome screen.py"])

window = tk.Tk()
window.geometry("350x100")
window.title("login to UBA ng")

phone_label = tk.Label(window, text="Enter Your Phone Number:")
phone_label.grid(row=0, column=0, sticky="nsew")

phone_entry = tk.Entry(window,width=15)
phone_entry.grid(row=0, column=1, sticky="nsew")

password_label = tk.Label(window, text='Enter Your Password:')
password_label.grid(row=1, column=0, sticky="nsew")

password_entry = tk.Entry(window, show="*", width=15)
password_entry.grid(row=1, column=1, sticky="nsew")

open_accounts_button = tk.Button(window, text=" LOGIN ", command=welcome, width= 15)
open_accounts_button.grid(row=3, column=1, sticky="nsew")
open_accounts_button.config(fg='#ffffff', bg='#de4343')

window.mainloop()