# Create the basics of the database
import pandas as pd

accPayable = pd.DataFrame()
accPayable["Name"] = []
accPayable["Date Paid"] = []
accPayable["Amount Paid"] = []
accPayable["Number of Weeks Paid"] = []

def addPayee():
    name = input("Enter the name of the member: ")
    date = input("Enter the date paid: ")
    amount = int(input("Enter the amount paid: "))
    weeksPaid = int(input("Enter number of weeks paid for: "))
    print()
    row = {"Name": name, "Date Paid": date, "Amount Paid": amount, "Number of Weeks Paid": weeksPaid}
    accPayable.loc[len(accPayable)] = row

def printDB():
    print(accPayable)
    print()

def calIncomeTotal():
    amountTotal = accPayable.iloc[:, 2]
    amountTotal.sum()

def printIncomeTotal():
    printDB()
    print("This month's total income is:", calIncomeTotal())
    print()

def clearDB():
    global accPayable
    accPayable = pd.DataFrame(columns=["Name", "Date Paid", "Amount Paid", "Number of Weeks Paid"])