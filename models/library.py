from user import User
from book import Book
from loan import Loan

class Library:
    """
    Represents a library management system.
    This class manages the collection of books, users,
    and loans. It provides methods to add, update,
    remove, search, borrow, and return books, as well
    as save and load the library data.
    """

    def __init__(self):
        """
        Initialize a new library.
        Creates empty collections for books, users,
        and loans.
        """
        self.__books = []
        self.__users = []
        self.__loans = []

    def add_book(self, book: Book) -> bool:
        """
        Add a book to the library.
        Args:
            book (Book): The book to add.
        Returns:
            bool: True if the book was successfully added,
            False otherwise.
        """
        if self.find_book(book.get_id()) is not None :   # si book existe on ne l'ajoute pas 
            return False
        
        self.__books.append(book)
        return True


    def remove_book(self, book_id: int) -> bool:
        """
        Remove a book from the library.
        Args:
            book_id (int): The unique identifier of the book.
        Returns:
            bool: True if the book was successfully removed,
            False otherwise.
        """
        book = self.find_book(book_id)
        if book is None:
            return False
        self.__books.remove(book)
        return True

    def update_book(
        self,
        book_id: int,
        title: str,
        author: str,
        category: str,
        year: int
    ) -> bool:
        """
        Update the information of an existing book.

        Args:
            book_id (int): The unique identifier of the book.
            title (str): The new title.
            author (str): The new author.
            category (str): The new category.
            year (int): The new publication year.

        Returns:
            bool: True if the book was successfully updated,
            False otherwise.
        """
        book = self.find_book(book_id)
        if book is None :
            return False
        book.set_title(title)
        book.set_author(author)
        book.set_category(category)
        book.set_year(year)
        return True

    def find_book(self, book_id: int) -> Book | None:
        """
        Find a book by its unique identifier.
        Args:
            book_id (int): The unique identifier of the book.
        Returns:
            Book | None: The matching book if found,
            otherwise None.
        """
        for b in self.__books:
            if b.get_id() == book_id  :
                return b
        return None

    def list_books(self) -> list[Book]:
        """
        Return all books in the library.
        Returns:
            list[Book]: A list containing all books.
        """
        return self.__books

    def add_user(self, user: User) -> bool:
        """
        Add a new user to the library.

        Args:
            user (User): The user to add.

        Returns:
            bool: True if the user was successfully added,
            False otherwise.
        """
        pass

    def find_user(self, user_id: int) -> User | None:
        """
        Find a user by their unique identifier.

        Args:
            user_id (int): The unique identifier of the user.

        Returns:
            User | None: The matching user if found,
            otherwise None.
        """
        pass

    def list_users(self) -> list[User]:
        """
        Return all registered users.

        Returns:
            list[User]: A list containing all users.
        """
        pass

    def borrow_book(self, user_id: int, book_id: int) -> bool:
        """
        Allow a user to borrow a book.

        The method verifies that the user and the book
        exist and that the book is available before
        creating a new loan.

        Args:
            user_id (int): The unique identifier of the user.
            book_id (int): The unique identifier of the book.

        Returns:
            bool: True if the borrowing operation was successful,
            False otherwise.
        """
        pass

    def return_book(self, user_id: int, book_id: int) -> bool:
        """
        Process the return of a borrowed book.

        Updates the book's availability and closes
        the corresponding loan.

        Args:
            user_id (int): The unique identifier of the user.
            book_id (int): The unique identifier of the book.

        Returns:
            bool: True if the return operation was successful,
            False otherwise.
        """
        pass

    def list_loans(self) -> list[Loan]:
        """
        Return all recorded loans.

        Returns:
            list[Loan]: A list containing all loans.
        """
        pass

    def save(self):
        """
        Save the library data.

        Stores books, users, and loans in persistent
        storage (e.g., JSON files).
        """
        pass

    def load(self):
        """
        Load the library data.

        Restores books, users, and loans from
        persistent storage.
        """
        pass
    
