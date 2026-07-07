from datetime import datetime
birth_year = int(input("Enter Your Birth Year: "))

current_year = datetime.now().year

age = current_year - birth_year

print("Current year =", current_year)
print("Your Age is =", age, "Years")
