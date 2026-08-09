class Book :
    def __init__(self,id:int, titre:str, auteur:str, categorie:str, annee:str ,disponible:str ):
        self.__id = id
        self.__titre = titre
        self.__auteur = auteur
        self.__categorie = categorie
        self.__annee = annee
        self.__disponible = disponible
    
    def afficher(self):
        pass

    def estDisponible(self):
        pass