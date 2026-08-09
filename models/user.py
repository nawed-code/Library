from person import Person



class User(Person):
    def __init__(self,id,nom,prenom,email ):
        Person.__init__(self,id, nom, prenom, email)
        self.__borrowed_book = []
    
    def emprunter(self):
        pass

    def retourner(self):
        pass


