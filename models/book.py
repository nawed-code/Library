from datetime import datetime

class Book:
    """
    Represents a book in the library.
    A book contains information about its title, author,
    category, publication year, and availability status.
    """

    def __init__(
        self,
        id: int,
        title: str,
        author: str,
        category: str,
        year: int,
        available: bool
    ):
        """
        Initialize a new book.

        Args:
        id (int): Unique identifier of the book.
        title (str): Title of the book.
        author (str): Author of the book.
        category (str): Book category or genre.
        year (int): Publication year.
        available (bool): Availability status of the book.
        """
        self.__id = id
        self.set_title(title)
        self.set_author(author)
        self.set_category(category)
        self.set_year(year)
        self.__available = available


    def get_id(self) -> int:
        """ return the book's id """
        return self.__id
    
    def get_title(self) -> str:
        """ return the book's title """
        return self.__title
    
    def get_author(self) -> str:
        """ return the book's author """
        return self.__author
    
    def get_category(self) -> str:
        """ return the book's category """
        return self.__category
    
    def get_year(self) -> int:
        """ return the publish year of the book """
        return self.__year
    
    def set_title(self,new_title):
        """ set a new title for book """
        if not new_title.strip():
            raise ValueError("The title cannot be empty.")
        self.__title = new_title

    def set_author(self,new_author : str):
        """ set a new author for book """
        if not new_author.strip():
            raise ValueError("The author cannot be empty")
        self.__author = new_author

    def set_category(self,new_category : str):
        """ set a new category """
        if not new_category.strip():
            raise ValueError("The category cannot be empty")
        self.__category = new_category

    def set_year(self,new_year:int):
        """ set a new year for book """
        currently_year = datetime.now().year()
        if new_year < 1450 or new_year > currently_year:
            raise ValueError("Invalid publication year !")
        self.__year = new_year

    def change_availability(self):
        """ Change the availability of book """
        self.__available = not self.__available

    def show(self):
        """
        Display the book's information.
        """
        print(f"""{{
            ID :            {self.__id},
            Title :         {self.__title},
            Author:         {self.__author},
            Category:       {self.__category},
            Year :          {self.__year},
            Available :     {self.__available}
        }}""")

    def is_available(self) -> bool:
        """
        Check whether the book is available for borrowing.
        Returns: bool: True if the book is available, False otherwise.
        """
        return self.__available
    
    def __str__(self) -> str:
        return f"{self.__title} {self.__year}" 