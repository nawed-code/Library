

class Person :
    def __init__(self,id : int, nom : str, prenom : str, email :str ):
        self.__id = id
        self.__nom = nom
        self.__prenom = prenom
        self.__email = email

    def afficher(self):
        
        print(f""" {{
            id : {self.__id},
            nom : {self.__nom},
            prénom : {self.__prenom},
            email address : {self.__email}
            
        }}""")

p1 = Person(1, "Dupont", "Jean", "jean@gmail.com")
p1.afficher()