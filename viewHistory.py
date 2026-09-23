def view_history(account_number, accounts):

    Transactions = accounts[account_number]["Transactions"]

    print("<----TRANSACTION HISTORY---->")

    if not Transactions:
        print("No transactions found")
        return


    for transaction in Transactions:
        print(
            transaction["type"],
            transaction["amount"],
            transaction["date"]
        )