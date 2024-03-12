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
    amount = int(input("Enter amount of expense: "))
    monthOverdue = int(input("Enter number of months overdue: "))
    row = {"Due Date": dueDate, "Expense": expense, "Remaining Balance": amount, "Month Overdue": monthOverdue}
    debtDB.loc[len(debtDB)] = row

def printDB():
    print(debtDB)

def payBalance():
    printDB()
    rowNum = int(input("Enter row number of expense to pay off: "))
    payBack = int(input("Enter amount to pay back: "))
    debtDB.at[rowNum, "Remaining Balance"] = debtDB.at[rowNum, "Remaining Balance"] - payBack

    if debtDB.at[rowNum, "Remaining Balance"] == 0:
        debtDB.drop(index=rowNum, inplace=True)

    printDB()