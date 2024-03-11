# Create the basics of the database
import pandas as pd

#Task 1
debtDB = pd.DataFrame()
debtDB['Due Date'] = []
debtDB['Expense'] = []
debtDB['Remaining Balance'] = []
debtDB['Month Overdue'] = []

def main():
    print(debtDB)

if __name__ == "__main__":
    main()