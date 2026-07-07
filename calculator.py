num1 = float(input("enter first number"))
num2 = float(input("enter second number"))
operation = input("Choose operation(+, -, *, /): ")
if operation == "+":
    print("Result =", num1 + num2)
elif operation == "-":
    print("Result =", num1 - num2) 
elif operation == "*":
    print("Result =", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("0 se divide nahi kar sakte")
else:
    print("Galat operation")




