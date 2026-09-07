from person import Person


class Librarian(Person):
    """
    Represents a librarian.
    A librarian is responsible for managing the library's
    collection of books. They can add, update, and remove
    books from the library.
    """

    def __init__(self, id, nom, prenom, email):
        """
        Initialize a new librarian.
        Args:
            id (int): Unique identifier of the librarian.
            nom (str): Librarian's last name.
            prenom (str): Librarian's first name.
            email (str): Librarian's email address.
        """
        super().__init__(id, nom, prenom, email)

    def add_book(self,library,book):
        """
        Add a new book to the library collection.
        Returns:
            bool: True if the book was successfully added,
            False otherwise.
        """
        return library.add_book(book)

    def remove_book(self,library,book_id):
        """
        Remove a book from the library collection.
        Returns:
            bool: True if the book was successfully removed,
            False otherwise.
        """
        return library.remove_book(book_id)
        

    def update_book(self,library,book_id):
        """
        Update the information of an existing book.
        Returns:
            bool: True if the book information was successfully updated,
            False otherwise.
        """
        return library.update_book(book_id)