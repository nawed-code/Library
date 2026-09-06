from user import User
from book import Book
from loan import Loan

class Library:
    def __init__(self):
        self.__books = []
        self.__users = []
        self.__loans = []

    def add_book(self, book: Book) -> bool:
        pass
    
    def remove_book(self,book_id :int) -> bool:
        pass
    
    def update_book(self,book_id: int,title: str,author: str,category: str,year: int) -> bool:
        pass
    
    def find_book(self, book_id: int) -> Book | None:
        pass
    
    def list_books(self) -> list[Book]:
        pass
    
    def add_user(self,user:User ) -> bool:
        pass
    
    def find_user(self, user_id: int) -> User | None:
        pass
    
    def list_users(self) -> list[User]:
        pass
    
    def borrow_book(self, user_id: int, book_id: int) -> bool:
        pass
    
    def return_book(self, user_id: int, book_id: int) -> bool:
        pass
    
    def list_loans(self) -> list[Loan]:
        pass
    
    def save(self):
        pass
    
    def load(self):
        pass
    
