# SIM TOOLKIT(M-PESA) logic

print("**Safaricom SIM toolkit**")
print("")

print("# Safaricom+")
print("# M-PESA")

phoneNo = "0703382631"
name = "George Odero"
balance = 10000
pin = 1234

choice = input("Enter the your choice: ")

if choice == "Safaricom":
    print("Welcome to Safaricom")
elif choice == "M-PESA":
    print("# Send Money")
    print("# Withdraw Cash")
    print("# Buy Airtime")
    print("# Loans and Savings")
    print("# Lipa na M-PESA")
    print("# My Account")

    choices = input("Choose one option: ")

    # Sending money
    if choices == "Send Money":
        phoneNo = input("Enter phone no(07***): ")
        if len(phoneNo) == 10 and phoneNo.startswith("07") and name == "George Odero":
            amount = float(input("Enter amount: "))
            balance = balance - amount
            print(f"Sending {amount} to {name}")
            print(f"Transaction Successfully. Your balance {balance}")
        else:
            print("Invalid phone no")
    
    # Withdraw cash
    elif choices == "Withdraw Cash":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance and amount > 0:
            balance = balance - amount
            print("Withdraw successful. New balance:", balance)
        else:
            print("Insufficient funds")

    # Buy Airtime
    elif choices == "Buy Airtime":
        amount = float(input("Enter airtime amount: "))
        if amount <= balance and amount > 0:
            balance -= amount
            print(f"Airtime purchase successful. New balance: {balance}")
        else:
            print("Insufficient funds or invalid amount.")

    # My Account
    elif choices == "My Account":
        print("# M-PESA PIN Manager")
        print("# Check Balance")

        option = input("Choose one option: ")

        # Pin management
        if option == "M-PESA PIN Manager":
            print("Change PIN")
            new_pin = input("Enter new PIN: ")
            pin = new_pin
            print("PIN changed successfully.")
            
        # Balance    
        elif option == "Check Balance":
            entered_pin = input("Enter M-PESA PIN: ")
            if entered_pin == str(pin):
                print(f"Your balance is {balance}") 
            else:
                print("Incorrect PIN. Try Again")

    else:
        print("Invalid Option") 
else:
    print("Thank you for using MPESA")                     





            




