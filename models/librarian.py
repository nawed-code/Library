from person import Person


class Librarian(Person):
    def __init__(self,id,nom,prenom,email):
        super().__init__(id,nom,prenom,email)

    def ajouterLivre(self):
        pass

    def supprimerLivre(self):
        pass

    def modifierLivre(self):
        pass


