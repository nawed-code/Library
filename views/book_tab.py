
from PySide6.QtWidgets import QWidget, QLineEdit,QVBoxLayout,QLabel,QPushButton,QMessageBox,QHBoxLayout,QTableWidget,QTableWidgetItem
from .book_management.add_book_window import AddBookWindow
from .book_management.remove_book_window import RemoveBookWindow
from .book_management.update_book_window import UpdateBookWindow
from models.book import Book


class BookTab(QWidget):

    def __init__(self,library):
        super().__init__()

        self.setWindowTitle("Book Management")
        self.resize(800, 600)
        self.library = library

        layout_searche = QHBoxLayout()
        layoutH = QHBoxLayout()          
        layout_principale = QVBoxLayout()   # container

        #   @@@@@@@@@@@@@@@@@@      searche bar     @@@@@@@@@@@@@@@@@@@@@@
        searcheLabel = QLabel("Searche : ")
        self.searcheInput = QLineEdit()
        searcheButton = QPushButton("Searche",self)

        layout_searche.addWidget(searcheLabel)
        layout_searche.addWidget(self.searcheInput)
        layout_searche.addWidget(searcheButton)

        #   @@@@@@@@@@@@@@@@@@      buttons     @@@@@@@@@@@@@@@@@@@@@@
        addButton = QPushButton("Add Book", self)
        deleteButton = QPushButton("Delete Book",self)
        updateButton = QPushButton("Update",self)

        #   @@@@@@@@@@@@@@@@@@      table     @@@@@@@@@@@@@@@@@@@@@@
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID","Title","Author", "Category","Year","Available"])
        self.list_book = self.library.list_books()
        taille =len(self.list_book)
        self.table.setRowCount(taille)
        for i in range(taille):
            self.table.setItem(i, 0, QTableWidgetItem(f"{self.list_book[i].get_id()}"))
            self.table.setItem(i, 1, QTableWidgetItem(self.list_book[i].get_title()))
            self.table.setItem(i, 2, QTableWidgetItem(self.list_book[i].get_author()))
            self.table.setItem(i, 3, QTableWidgetItem(self.list_book[i].get_category()))
            self.table.setItem(i, 4, QTableWidgetItem(f"{self.list_book[i].get_year()}"))
            self.table.setItem(i, 5, QTableWidgetItem(f"{self.list_book[i].is_available()}"))
        layout_principale.addWidget(self.table)   # ajoute la table 

        #   @@@@@@@@@@@@@@@@@@       container     @@@@@@@@@@@@@@@@@@@@@@

        layoutH.addWidget(addButton)
        layoutH.addWidget(deleteButton)
        layoutH.addWidget(updateButton)

        layout_principale.addLayout(layout_searche)
        layout_principale.addLayout(layoutH)

        self.setLayout(layout_principale)

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
   

        