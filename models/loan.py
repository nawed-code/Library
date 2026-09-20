from book import Book
from user import User
from datetime import datetime


class Loan:
    """
    Represents a book loan in the library.
    A loan links a user to a book for a specific period of time.
    It records the borrowing date and the return date once the
    book has been returned.
    """

    def __init__(
        self,
        borrowing_date: datetime,
        return_date: datetime | None,
        due_date : datetime,
        user: User,
        book: Book
    ):
        """
        Initialize a new loan.
        Args:
            borrowingDate (datetime): The date and time when the book was borrowed.
            returnDate (datetime | None): The date and time when the book was returned.
            Use None if the book has not yet been returned.
            user (User): The user who borrowed the book.
            book (Book): The borrowed book.
        """
        self.__borrowingDate = borrowing_date
        self.__returnDate = return_date
        self.__due_date = 
        self.__user = user
        self.__book = book

    """ getters """

    def get_user(self):
        """ return the user"""
        return self.__user
    
    def get_book(self):
        """ return the book """
        return self.__book
    
    def get_borrowed_date(self):
        """ return the borrowing date """
        return self.__borrowingDate
    
    def get_return_date(self):
        """ return the date of return """
        return self.__returnDate

    def is_late(self) -> bool :
        """
        Check whether the loan is overdue.
        Returns:bool: True if the loan is overdue, False otherwise.
        """
        if self.__returnDate == None:
            return False
        return datetime.now() > self.__returnDate
       
        

    def duration(self) -> int : 
        """
        Calculate the duration of the loan.
        Returns:
            int: The number of days since the book was borrowed.
        """
        return (datetime.now() - self.__borrowingDate).days
    

    def __str__(self) -> str:
        return f"{self.__user} borrowed {self.__book}"