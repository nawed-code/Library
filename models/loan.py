from book import Book
from user import User
from datetime import datetime



class Loan:

    def __init__(self,dateEmprunt:datetime , dateRetour , utilisateur:User, livre:Book):
        self.__date_emprunt = dateEmprunt
        self.__date_retour = dateRetour
        self.__utilisateur = utilisateur
        self.__livre = livre

    
    def estEnRetard(self):
        pass

    def duree(self):
        pass

