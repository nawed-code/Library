class Person:
    """
    Represents a person in the library.
    This is the base class for all people in the library system,
    including users and librarians. It stores the common personal
    information shared by all of them.
    """

    def __init__(self, id: int, nom: str, prenom: str, email: str):
        """
        Initialize a new person.

        Args:
            id (int): Unique identifier of the person.
            nom (str): Person's last name.
            prenom (str): Person's first name.
            email (str): Person's email address.
        """
        self.__id = id
        self.__nom = nom
        self.__prenom = prenom
        self.__email = email

    def get_name(self):
        """ give the first name """
        return self.__prenom

    def get_last_name(self):
        """ give the last name """
        return self.__nom
    
    def get_id(self):
        """ give the id """
        return self.__id
    
    def get_email(self):
        """ give the addres email"""
        return self.__email

    def set_email(self,new_email :str):
        """ set a new adress email """    
        if "@" not in new_email :
            raise ValueError("Invalid email address")
        self.__email = new_email

    def set_name(self, new_name: str):
        """ set a new name """
        if new_name =="" :
            raise ValueError("Invalid name")
        self.__prenom = new_name

    def set_last_name(self,new_last_name : str):
        """ set a new last name """
        if new_last_name == "":
            raise ValueError("Invalid last name")
        self.__prenom = new_last_name    

        
    def get_information(self):
        """
        Display the person's information.
        """
        print(f"""
        {{
            id : {self.__id},
            nom : {self.__nom},
            prénom : {self.__prenom},
            email address : {self.__email}
        }}
        """)

    def __str__(self):
        return f'{self.__prenom} {self.__nom}'
