books = []

while True:
    print("\n1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display All Books")
    print("5. Total Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully.")

    elif choice == "2":
        book = input("Enter book name to remove: ")
        if book in books:
            books.remove(book)
            print("Book removed successfully.")
        else:
            print("Book not found.")

    elif choice == "3":
        book = input("Enter book name to search: ")
        if book in books:
            print("Book is available.")
        else:
            print("Book not found.")

    elif choice == "4":
        if len(books) == 0:
            print("No books available.")
        else:
            print("Books in Library:")
            for book in books:
                print(book)

    elif choice == "5":
        print("Total books available:", len(books))

    elif choice == "6":
        print("Exiting Library Management System...")
        break

    else:
        print("Invalid choice. Please try again.")