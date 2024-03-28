# Dateframe for the monthly income statement
import pandas as pd
import Donovan_task2

incomeStatement = pd.DataFrame()
incomeStatement["Type"] = []
incomeStatement["Name"] = []
incomeStatement["Amount"] = []

def addRevenue():
    name = input("Enter the type of revenue: ")
    amount = int(input("Enter the amount of revenue: "))

    print()
    row = {"Type": "Revenue", "Name": name, "Amount": amount}
    incomeStatement.loc[len(incomeStatement)] = row

def printDB():
    print(incomeStatement)
    print()

def calIncomeTotal():
    printDB()
    amountTotal = incomeStatement.iloc[:, 3]
    print("This month's total income is:",amountTotal.sum())
    print()

def clearDB():
    global incomeStatement
    incomeStatement = pd.DataFrame(columns=["Type", "Name", "Amount"])