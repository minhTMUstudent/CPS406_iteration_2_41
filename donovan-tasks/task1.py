# Create the basics of the database
import pandas as pd

debtDB = pd.DataFrame()
debtDB["Due Date"] = []
debtDB["Expense"] = []
debtDB["Remaining Balance"] = []
debtDB["Month Overdue"] = []

def addExpense():
    dueDate = input("Enter the due date: ")
    expense = input("Enter type of expense: ")
    amount = input("Enter amount of expense: ")
    monthOverdue = input("Enter number of months overdue: ")
    row = {"Due Date": dueDate, "Expense": expense, "Remaining Balance": amount, "Month Overdue": monthOverdue}
    debtDB.loc[len(debtDB)] = row

def printDB():
    print(debtDB)

addExpense()
printDB()