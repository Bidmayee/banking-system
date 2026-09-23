# LOGIN PAGE 
from accountMenu import account_menu
def login(accounts):
    account_number = input("Enter your Account number : ")
    pin = input("Enter your PIN : ")

    if account_number in accounts:
        if accounts[account_number]["PIN"] == pin:
            print("Login sucessfully !!!!")
            account_menu(account_number,accounts)
            
        else:
            print("Invalid PIN, Enter Correct PIN....")
    else:
        print("Account not found")