while True:
    print("/n===== STUDENT MANAGEMENT SYSTEM =====")
    print("    print()")
    print("2. View Stuedent")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice")

    if choice == "1":
        print("Add Student")

    elif choice == "2":
        print("View Student")

    elif choice == "3":
        print("Delete Student")

    elif choice == "4":
        print("Search Student")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid Choice")