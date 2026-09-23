from checkBalance import check_balance
from deposit import deposit
from withdraw import withdraw
from transfer import transfer
from viewHistory import view_history
from changePin import change_pin
def account_menu(account_number, accounts):
    while True:
        print("<-----ACCOUNT MENU----->")
        print("1.Check Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Transfer")
        print("5.Transaction History")
        print("6.Change PIN")
        print("7.Logout")


        choice = input("Enter Your Choice: ")

        if choice == "1":
            check_balance(account_number, accounts)
        
        elif choice == "2":
            deposit(account_number, accounts)

        elif choice == "3":
            withdraw(account_number, accounts)

        elif choice == "4":
            transfer(account_number, accounts)

        elif choice == "5":
            view_history(account_number, accounts)

        elif choice == "6":
            change_pin(account_number, accounts)
        
        elif choice == "7":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice.")
                       





