import json
import os
from tkinter import Tk, Label, Entry, Button, Text, END
from datetime import datetime

FILE_NAME = 'expenses.json'


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILE_NAME, 'w') as file:
        json.dump(expenses, file)


def add_expense(date, description, amount):
    expenses = load_expenses()
    expenses.append({
        'date': date,
        'description': description,
        'amount': amount
    })
    save_expenses(expenses)


def add_expense_gui():
    date = date_entry.get()
    description = description_entry.get()
    amount = amount_entry.get()

    try:
        amount = float(amount)
        add_expense(date, description, amount)
        result_text.insert(END, f"Added: {date} - {description} - ${amount:.2f}\n")
        date_entry.delete(0, END)
        description_entry.delete(0, END)
        amount_entry.delete(0, END)
    except ValueError:
        result_text.insert(END, "Invalid amount. Please enter a number.\n")


def view_expenses_gui():
    expenses = load_expenses()
    result_text.delete(1.0, END)

    if not expenses:
        result_text.insert(END, "No expenses found.\n")
        return

    for expense in expenses:
        result_text.insert(END,
                           f"Date: {expense['date']}, Description: {expense['description']}, Amount: ${expense['amount']:.2f}\n")


# Setting up the GUI
root = Tk()
root.title("Expense Tracker")

Label(root, text="Date (YYYY-MM-DD):").grid(row=0, column=0)
date_entry = Entry(root)
date_entry.grid(row=0, column=1)

Label(root, text="Description:").grid(row=1, column=0)
description_entry = Entry(root)
description_entry.grid(row=1, column=1)

Label(root, text="Amount:").grid(row=2, column=0)
amount_entry = Entry(root)
amount_entry.grid(row=2, column=1)

Button(root, text="Add Expense", command=add_expense_gui).grid(row=3, column=0, columnspan=2)
Button(root, text="View Expenses", command=view_expenses_gui).grid(row=4, column=0, columnspan=2)

result_text = Text(root, width=50, height=10)
result_text.grid(row=5, column=0, columnspan=2)

root.mainloop()
