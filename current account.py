import tkinter as tk

#def print_on_screen():


class BankAccount:
    def __init__(self):
        self.balance = 10000000

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):

        if self.balance >= amount:
            self.balance -= amount
        else:
            my_lbl = tk.Label(window, text="Insufficient funds.")
            my_lbl.grid(row=4, column=2)

window = tk.Tk()
window.geometry("500x100")
window.title("current Accounts")
current_account = BankAccount()

def deposit_to_current():
    amount = float(current_entry.get())
    current_account.deposit(amount)
    current_balance.config(text=f"Current Account Balance: {current_account.balance}")

def withdraw_from_current():
    amount = float(current_entry.get())
    current_account.withdraw(amount)
    current_balance.config(text=f"Current Account Balance: {current_account.balance}")

current_label = tk.Label(window, text="Current Account")
current_label.grid(row=3, column=0, sticky="nsew")

current_entry = tk.Entry(window)
current_entry.grid(row=3, column=1, sticky="nsew")

current_deposit_button = tk.Button(window, text="Deposit", command=deposit_to_current)
current_deposit_button.grid(row=3, column=2, sticky="nsew")
current_deposit_button.config(fg='#ffffff', bg='#de4343')

current_withdraw_button = tk.Button(window, text="Withdraw", command=withdraw_from_current)
current_withdraw_button.grid(row=3, column=3, sticky="nsew")
current_withdraw_button.config(fg='#ffffff', bg='#de4343')

current_balance = tk.Label(window, text="Current Account Balance: 10000000")
current_balance.grid(row=4, column=0, sticky="nsew")

window.mainloop()