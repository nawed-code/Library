
from PySide6.QtWidgets import QWidget, QLineEdit,QVBoxLayout,QLabel,QPushButton,QMessageBox,QHBoxLayout,QTabWidget
from .book_management.add_book_window import AddBookWindow
from .book_management.remove_book_window import RemoveBookWindow
from .book_management.update_book_window import UpdateBookWindow


class BookTab(QWidget):

    def __init__(self,library):
        super().__init__()

        self.setWindowTitle("Book Management")
        self.resize(800, 600)
        self.library = library

        layoutH = QHBoxLayout()         # container 
        
        #   @@@@@@@@@@@@@@@@@@      searche bar     @@@@@@@@@@@@@@@@@@@@@@
        searcheLabel = QLabel("Searche : ")
        self.searcheInput = QLineEdit()

        #   @@@@@@@@@@@@@@@@@@      buttons     @@@@@@@@@@@@@@@@@@@@@@
        searcheButton = QPushButton("Searche",self)
        addButton = QPushButton("Add Book", self)
        deleteButton = QPushButton("Delete Book",self)
        updateButton = QPushButton("Update",self)

        #   @@@@@@@@@@@@@@@@@@      elements du container     @@@@@@@@@@@@@@@@@@@@@@
        layoutH.addWidget(searcheLabel)
        layoutH.addWidget(self.searcheInput)
        layoutH.addWidget(searcheButton)

        layoutH.addWidget(addButton)
        layoutH.addWidget(deleteButton)
        layoutH.addWidget(updateButton)
        self.setLayout(layoutH)

        #   @@@@@@@@@@@@@@@@@@      fonctions      @@@@@@@@@@@@@@@@@@@@@@
        searcheButton.clicked.connect(self.searche_book)
        addButton.clicked.connect(self.add_book)
        deleteButton.clicked.connect(self.remove_book)
        updateButton.clicked.connect(self.update_book)

        #           --------------  méthode pour les boutons -------------------
    
    def searche_book(self):
        pass

    def add_book(self):                                     #ajoute book
        self.add_book_window = AddBookWindow(self.library)
        self.add_book_window.show()
        

    def remove_book(self):                                  #remove book
        self.remove_book_window = RemoveBookWindow(self.library)
        self.remove_book_window.show()
    
    def update_book(self):
        self.update_book_window = UpdateBookWindow(self.library)
        self.update_book_window.show()
        #print("update clicked")
   

        