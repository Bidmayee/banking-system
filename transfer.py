def transfer(sender_acc, accounts):
    receiver_acc = input("Enter account number of receiver")

    if receiver_acc not in accounts:
        print("Receiver not found")
        return

    if receiver_acc == sender_acc :
        print("Not possible ")
        return

    amount = float(input("Enter amount to transfer: "))

    if amount <=0:
        print("Amount must be greater than 0")
        return

    if amount > accounts[sender_acc]["Balance"]:
        print("Insufficient balance")
        return

    accounts[sender_acc]["Balance"] -= amount
    accounts[receiver_acc]["Balance"] += amount

    print("Transfer successful")