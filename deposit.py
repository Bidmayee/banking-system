def deposit(account_number, accounts):

    amount = float(input("Enter amount to deposit: "))

    if amount <=0:
        print("Amount must be more than 0 ")
        return

    accounts[account_number]["Balance"] += amount

    print("Deposit successful !!!!!")
    print("Your current balance is ", accounts[account_number]["Balance"])