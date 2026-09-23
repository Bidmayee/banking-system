from datetime import datetime
def withdraw(account_number , accounts):

    amount = float(input("Enter amount to withdraw: "))

    if amount <=0:
        print("Amount must be more than 0 ")
        return

    balance = accounts[account_number]["Balance"]

    if amount > balance:
        print("Insufficient balance.")
        return

    accounts[account_number]["Balance"] -= amount

    transaction = {
        "type": "Withdrawal",
        "amount": amount,
        "date": datetime.now()
    }

    accounts[account_number]["Transactions"].append(transaction)

    print("withdraw successful !!!!!")
    print("Your current balance is ", accounts[account_number]["Balance"])
