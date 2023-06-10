import tkinter as tk

class BankAccount:
    def __init__(self):
        self.balance = 10000000

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > 200000:
            my_lbl = tk.Label(window, text="Withdrawal amount exceeds the limit.")
            my_lbl.grid(row=5, column=0, sticky="nsew")

        elif self.balance >= amount:
            self.balance -= amount
        else:
            my_lbl = tk.Label(window, text="Insufficient funds.")
            my_lbl.grid(row=4, column=2, sticky="nsew")

window = tk.Tk()
window.geometry("500x100")
window.title("savings Account")
savings_account = BankAccount()

def deposit_to_savings():
    amount = float(savings_entry.get())
    savings_account.deposit(amount)
    savings_balance.config(text=f"Savings Account Balance: {savings_account.balance}")

def withdraw_from_savings():
    amount = float(savings_entry.get())
    savings_account.withdraw(amount)
    savings_balance.config(text=f"Savings Account Balance: {savings_account.balance}")

savings_label = tk.Label(window, text="Savings Account")
savings_label.grid(row=3, column=0, sticky="nsew")

savings_entry = tk.Entry(window)
savings_entry.grid(row=3, column=1, sticky="nsew")

savings_deposit_button = tk.Button(window, text="Deposit", command=deposit_to_savings)
savings_deposit_button.grid(row=3, column=2, sticky="nsew")
savings_deposit_button.config(fg='#ffffff', bg='#de4343')

savings_withdraw_button = tk.Button(window, text="Withdraw", command=withdraw_from_savings)
savings_withdraw_button.grid(row=3, column=3, sticky="nsew")
savings_withdraw_button.config(fg='#ffffff', bg='#de4343')

savings_balance = tk.Label(window, text="Savings Account Balance: 10000000")
savings_balance.grid(row=4, column=0, sticky="nsew")

window.mainloop()