balance = 10000

print("Welcome to ATM")

choice = input("1. Check Balance\2. Deposit\n3. Withdraw\nEnter Choice: ")

if choice == "1":
    print("Your Balance =", balance)
elif choice == "2":
    amount = float(input("Enter Deposit Amount: "))
    balance = balance + amount
    print("New Balance =", balance)

