from PySide6.QtWidgets import QWidget, QLineEdit,QVBoxLayout,QLabel,QPushButton,QMessageBox,QHBoxLayout,QTabWidget

class HomeTab(QWidget):

    def __init__(self,library):
        super().__init__()
        self.resize(800, 600)
        self.library = library

        layout = QVBoxLayout()          #container 
        welcome_label = QLabel("Welcome !")
        layout.addWidget(welcome_label)

        information_label = QLabel("This application allows you to manage:    ✔ Books,   ✔ Users,    ✔ Loans")
        layout.addWidget(information_label)

        self.book_count = len(self.library.list_books())
        book_count_label = QLabel(f"📚 Books : {self.book_count}")

        self.user_count = len(self.library.list_users())
        user_count_label = QLabel(f"👤 Users : {self.user_count}")

        self.loans_count = len(self.library.list_loans())
        loan_count_label = QLabel(f"📖 Borrowed books : {self.loans_count}")

        layout.addWidget(book_count_label)
        layout.addWidget(user_count_label)
        layout.addWidget(loan_count_label)


        self.setLayout(layout)