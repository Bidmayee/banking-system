def change_pin(account_number , accounts):

    old_pin = input("Enter old PIN: ")

    if old_pin != accounts[account_number]["PIN"]:
        print("Incorrect PIN")
        return

    new_pin = input("Enter new 4-digit PIN: ")
    confirm_pin = input("Confirm new PIN: ")

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must contain exactly 4 digits")
        return

    if new_pin != confirm_pin:
        print("PIN do not match")
        return

    accounts[account_number]["PIN"] = new_pin

    print("PIN changed successfully !!!!")