from PySide6.QtWidgets import QWidget, QLineEdit,QVBoxLayout,QLabel,QPushButton,QMessageBox

class BorrowBookWindow(QWidget):

    def __init__(self,library):
        super().__init__()
        self.library = library

        self.setWindowTitle("Borrow a book")
        self.resize(300,200)

        user_id_label = QLabel("User id :")
        self.user_id_input = QLineEdit()

        book_id_label = QLabel("Book id :")
        self.book_id_input = QLineEdit()

        button = QPushButton("Borrow",self)
        button.clicked.connect(self.borrow_book)

        layout = QVBoxLayout()
        layout.addWidget(user_id_label)
        layout.addWidget(self.user_id_input)
        layout.addWidget(book_id_label)
        layout.addWidget(self.book_id_input)
        layout.addWidget(button)

        self.setLayout(layout)
        

    def borrow_book(self):
        try:
            user_id = int(self.user_id_input.text())
            book_id = int(self.book_id_input.text())
        except ValueError:
            QMessageBox.warning(self,"Error","The  id should be a number")
            print("The id must be a number")
            return
        if self.library.borrow_book(user_id,book_id):
            self.library.save()
            print("Book borrowed successfully ")
            self.close()
        else:
            QMessageBox.warning(self,"Error","Please check the id or availability of the book")