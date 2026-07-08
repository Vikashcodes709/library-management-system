books = []

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        books.append({
            "id": book_id,
            "name": book_name,
            "author": author })
        print("Book Added Successfully!")

    elif choice == "2":
        if books:
            print("\n===== BOOK LIST =====")
            for book in books:
                print("----------------------")
                print("BOOK ID :", book["id"])
                print("Book Name :", book["name"])
                print("Author :", book["author"])
        else:
            print("No Books Available!")

    elif choice == "3":
        name = input("Enter Book Name: ")
        if name in books:
            print("Book Found!")
        else:
            print("Book Not Found!")
        
    elif choice == "4":
        name = input("Enter Book Name to Delete: ")
        if name in books:
            books.remove(name)
            print("Book Deleted!")
        else:
            print("Book Not Found!")

    elif choice == "5":
        name = input("Thank You! ")
        break

    else:
        print("Invalid Choice!")




    


    