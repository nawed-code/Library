from models.library import Library
from models.book import Book
from models.user import User
from models.loan import Loan
from models.librarian import Librarian

def main():
    library = Library()

    library.load()
    print("après load : ")
    print("\nUsers:")
    
    print("Books:")
    for book in library.list_books():
        book.show()

    print("\nUsers:")
    for user in library.list_users():
        user.get_information()

    print("\nLoans:")
    for loan in library.list_loans():
        print(loan)

    book1 = Book(3, "Java script", "Antoine de Saint-Exupéry", "Novel", 2000, True)
    book2 = Book(4, "1984", "George Orwell", "Science Fiction", 2011, True)

    library.add_book(book1)
    library.add_book(book2)

    user1 = User(1, "Dupont", "Jean", "jean@gmail.com")
    user2 = User(2, "Martin", "Alice", "alice@gmail.com")

    library.add_user(user1)
    library.add_user(user2)

    library.borrow_book(1, 1)

    print("Books:")
    for book in library.list_books():
        book.show()

    print("\nUsers:")
    for user in library.list_users():
        user.get_information()

    print("\nLoans:")
    for loan in library.list_loans():
        print(loan)

    library.save()


if __name__ == "__main__":
    main()