from createAccount import create_account
from login import login
def mainMenu(accounts):
    while True:

        print("<-------BANKING SYSTEM------->")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ") 

        if choice == "1" :
            create_account(accounts)

        elif choice == "2" :
            login(accounts)
        
        elif choice == "3" :
            print("EXIT")
            break
        
        else:
            print("Invalid choice.")
