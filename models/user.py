from .person import Person


class User(Person):
    """
    Represents a library user.

    A user can borrow, view, and return books.
    The user also maintains a list of currently borrowed books.
    """

    @classmethod
    def from_dict(cls,data):
        """
            Create a User object from a dictionary.
            Args:
                data (dict): A dictionary containing the person's data.
                    Expected keys are:
                    - "id" (int): The person's unique identifier.
                    - "last_name" (str): The person's last name.
                    - "name" (str): The person's first name.
                    - "email" (str): The person's email address.
            Returns:
                User: A new User instance initialized with the provided data.
        """
        return cls(data["id"],data["last_name"],data["name"],data["email"])
        
    

    def __init__(self, id, nom, prenom, email):
        """
        Initialize a new library user.

        Args:
            id (int): Unique identifier of the user.
            nom (str): User's last name.
            prenom (str): User's first name.
            email (str): User's email address.
        """
        super().__init__(id, nom, prenom, email)
        self.__borrowed_book = []

    def emprunter(self, book):
        """
        Borrow a book if it is available.
        Args:
            book (Book): The book to borrow.
        Returns:
            bool: True if the book was successfully borrowed,
            False otherwise.
        """
        self.__borrowed_book.append(book)
        

    def retourner(self, book):
        """
        Return a previously borrowed book.
        Args:
            book (Book): The book to return.
        Returns:
            bool: True if the book was successfully returned,
            False otherwise.
        """
        pass

    def to_dict(self) -> dict:
        """
        Convert the user into a dictionary.
        Returns:
        dict: A dictionary containing the user's information,
        including the borrowed books.
        """
        return {
            "id":self.get_id(),
            "last_name":self.get_last_name(),
            "name":self.get_name(),
            "email":self.get_email()
        }