# CREATE YOUR ACCOUNT 
import random

def create_account(accounts):
    print("CREATE YOUR ACCOUNT")

    name  = input("Enter Your Name : ")
    phone = input("Enter Your Number : ")

    while True :
         pin   = input("Create Your 4-digit PIN : ")

         if pin.isdigit() and len(pin) == 4:
            break
 

    while True :
        account_number = str(random.randint(10000,999999))
        if account_number not in accounts:
           break


    accounts[account_number] = {
        "Name" : name,
        "PhoneNo" : phone,
        "PIN" : pin,
        "Balance" : 0,
        "Transactions" : []
    }

    print("Your account created successfully !!!!!!!!")
    print("Your Account number is : ", account_number) 