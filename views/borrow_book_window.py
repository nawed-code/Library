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
        pass