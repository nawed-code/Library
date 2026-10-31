from PySide6.QtWidgets import QWidget, QPushButton,QVBoxLayout, QHBoxLayout
from .add_book_window import AddBookWindow
from .remove_book_window import RemoveBookWindow
from .borrow_book_window import BorrowBookWindow 
#from .update_book_window import UpdateBookWindow
#from .return_book_window import ReturnBookWindow
class MainWindow(QWidget):

    def __init__(self,library):
        super().__init__()

        self.setWindowTitle("Library Management")
        self.resize(800, 600)
        self.library = library
        addButton = QPushButton("Add Book", self)
        deleteButton = QPushButton("Delete Book",self)
        borrowButton = QPushButton("Borrow",self)
        updateButton = QPushButton("Update",self)
        returnButton = QPushButton("Return",self)

        layoutH = QHBoxLayout()
        layoutH.addWidget(addButton)
        layoutH.addWidget(deleteButton)
        layoutH.addWidget(borrowButton)
        layoutH.addWidget(updateButton)
        layoutH.addWidget(returnButton)
        self.setLayout(layoutH)

        addButton.clicked.connect(self.add_book)
        deleteButton.clicked.connect(self.remove_book)
        borrowButton.clicked.connect(self.borrow_book)
        updateButton.clicked.connect(self.update_book)
        returnButton.clicked.connect(self.return_book)

        #           --------------  méthode pour les boutons -------------------
    
    def add_book(self):                                     #ajoute book
        self.add_book_window = AddBookWindow(self.library)
        self.add_book_window.show()
        

    def remove_book(self):                                  #remove book
        self.remove_book_window = RemoveBookWindow(self.library)
        self.remove_book_window.show()

    def borrow_book(self):
        self.borrow_book_window = BorrowBookWindow(self.library)
        self.borrow_book_window.show()
        #print("borrow clicked")

    def update_book(self):
        self.update_book_window = UpdateBookWindow(self.library)
        self.update_book_window.show()
        #print("update clicked")

    def return_book(self):
        self.return_book_window = ReturnBookWindow(self.library)
        self.retur_book_window.show()
        #print("return clicked")


    
        

        
