# Dateframe for the monthly income statement
import pandas as pd
import payeeDB_IT2 as payeeDB

incomeStatement = pd.DataFrame()
incomeStatement["Type"] = []
incomeStatement["Name"] = []
incomeStatement["Amount"] = []

def addIncome():
    type = input("Enter the type of income: ")
    name = input("Enter the name of income: ")
    amount = int(input("Enter the amount of income: "))
    print()
    row = {"Type": type, "Name": name, "Amount": amount}
    incomeStatement.loc[len(incomeStatement)] = row

def addTotalPayeeIncome():
    payeeIncome = payeeDB.calIncomeTotal()
    row = {"Type": "Revenue", "Name": "Payee Income", "Amount": payeeIncome}
    incomeStatement.loc[len(incomeStatement)] = row

def printDB():
    print(incomeStatement)
    print()

def calIncomeTotal():
    amountTotal = incomeStatement.iloc[:, 3]
    amountTotal.sum()

def printIncomeTotal():
    printDB()
    print("This month's total income is:", calIncomeTotal())
    print()

def clearAllDB():
    global incomeStatement
    incomeStatement = pd.DataFrame(columns=["Type", "Name", "Amount"])
    payeeDB.clearDB()