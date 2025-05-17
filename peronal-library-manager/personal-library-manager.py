import json
import os

# 🔹 File to Store Library Data
LIBRARY_FILE = "library.json"

# 🔹 Load Library from File (If Exists)
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

# 🔹 Save Library to File
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# 🔹 Add a New Book
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = input("Enter the publication year: ").strip()
    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read_status
    }

    library.append(book)
    save_library(library)
    print(f"\n✅ '{title}' added successfully!\n")

# 🔹 Remove a Book
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            print(f"\n✅ '{title}' removed successfully!\n")
            return
    print("\n❌ Book not found!\n")

# 🔹 Search for a Book (Title or Author)
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    query = input("Enter search term: ").strip().lower()

    matches = [book for book in library if query in book["title"].lower() or query in book["author"].lower()]

    if matches:
        print("\n📚 Matching Books:")
        for book in matches:
            status = "Read ✅" if book["read"] else "Unread ❌"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("\n❌ No matching books found.\n")

# 🔹 Display All Books
def display_books(library):
    if not library:
        print("\n📚 Your library is empty.\n")
        return

    print("\n📚 Your Library:")
    for i, book in enumerate(library, start=1):
        status = "Read ✅" if book["read"] else "Unread ❌"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# 🔹 Display Library Statistics
def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("\n📊 No books in the library.\n")
        return

    read_books = sum(book["read"] for book in library)
    percentage_read = (read_books / total_books) * 100

    print(f"\n📊 Library Statistics:\nTotal books: {total_books}\nPercentage read: {percentage_read:.2f}%\n")

# 🔹 Menu System
def main():
    library = load_library()

    while True:
        print("\n📖 Personal Library Manager\n1. Add a book\n2. Remove a book\n3. Search for a book\n4. Display all books\n5. Display statistics\n6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("\n📚 Library saved. Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice! Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    main()
