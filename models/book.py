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
            titre (str): Title of the book.
            auteur (str): Author of the book.
            categorie (str): Book category or genre.
            annee (int): Publication year.
            disponible (bool): Availability status of the book.
        """
        self.__id = id
        self.__title = title
        self.__author = author
        self.__category = category
        self.__year= year
        self.__available = available


    def get_id(self):
        """ return the book's id """
        return self.__id
    
    def get_title(self):
        """ return the book's title """
        return self.__title
    
    def get_author(self):
        """ return the book's author """
        return self.__author
    
    def get_category(self):
        """ return the book's category """
        return self.__category
    
    def get_year(self):
        """ return the publish year of the book """
        return self.__year
    
    def set_title(self,new_title):
        """ set a new title for book """
        if new_title == "":
            raise ValueError("The title cannot be empty.")
        self.__title = new_title

    
    def show(self):
        """
        Display the book's information.
        """
        print(f"""{{
            ID :            {self.__id},
            Title :         {self.__titre},
            Author:         {self.__author},
            Category:       {self.__category},
            Year :          {self.__year},
            Available :     {self.__available}
        }}""")

    def is_available(self):
        """
        Check whether the book is available for borrowing.
        Returns:
            bool: True if the book is available, False otherwise.
        """
        return self.__available
    
    def __str__(self):
        return f"{self.__title} {self.__year}" 