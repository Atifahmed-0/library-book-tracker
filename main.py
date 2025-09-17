def add_book(title):
    with open("library.txt", "a") as f:
        f.write(title + "\n")


def read_books():
    try:
        with open("library.txt", "r") as f:
            books = f.readlines()
            if not books:
                print("📂 No books found.\n")
            else:
                print("\n📚 List of Books:")
                for i, book in enumerate(books, 1):
                    print(f"{i}. {book.strip()}")
                print()
    except FileNotFoundError:
        print("📂 No library file found yet. Add a book first.\n")


while True:
    print("====== LIBRARY MENU ======")
    print("1. ➕ Add Book")
    print("2. 📖 View Books")
    print("3. 🚪 Exit")

    try:
        choice = int(input("Enter your choice (1-3): "))
    except ValueError:
        print("❌ Please enter a valid number.\n")
        continue

    if choice == 1:
        title = input("Enter book title: ")
        add_book(title)
        print("✅ Book added successfully!\n")

    elif choice == 2:
        read_books()

    elif choice == 3:
        print("👋 Exiting... Thank you for using the library system!")
        break

    else:
        print("❌ Invalid choice. Please try again.\n")
