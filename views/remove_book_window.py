from PySide6.QtWidgets import QWidget, QLineEdit,QVBoxLayout,QLabel,QPushButton,QMessageBox
from models.book import Book

class RemoveBookWindow(QWidget):

    def __init__(self,library):
        super().__init__()
        self.library = library

        self.setWindowTitle("Delete a book")
        self.resize(300,100)

        id_label = QLabel("Id :")
        self.id_input = QLineEdit()

        button = QPushButton("Delete",self)
        button.clicked.connect(self.remove_book)

        layout = QVBoxLayout()
        layout.addWidget(id_label)
        layout.addWidget(self.id_input)
        layout.addWidget(button)

        self.setLayout(layout)

    def remove_book(self):              # supprime un livre
        try:
            id = int(self.id_input.text())
        except ValueError:
            QMessageBox.warning(self,"Error","The id should be a number")
            return
        if self.library.remove_book(id):
            self.library.save()
            print("Book removed successfully")
            self.close()
            
        else:
            QMessageBox.warning(self,"Error","We could not find this book")
            return