from PySide6.QtWidgets import QWidget, QPushButton,QVBoxLayout, QHBoxLayout
from .add_book_window import AddBookWindow
class MainWindow(QWidget):

    def __init__(self,library):
        super().__init__()

        self.setWindowTitle("Library Management")
        self.resize(800, 600)
        self.library = library
        button1 = QPushButton("Add Book", self)
        button2 = QPushButton("Delete Book",self)

        layoutV = QVBoxLayout()

        layoutV.addWidget(button1)
        layoutV.addWidget(button2)

        self.setLayout(layoutV)

        button1.clicked.connect(self.add_book)
        button2.clicked.connect(self.remove_book)
    
    def add_book(self):
        add_book_window = AddBookWindow(self.library)
        add_book_window.show()
        print("book added")

    def remove_book(self):
        print("book removed")

        
