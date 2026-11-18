from PySide6.QtWidgets import QWidget, QLineEdit,QVBoxLayout,QLabel,QPushButton,QMessageBox,QHBoxLayout,QTabWidget

class HomeTab(QWidget):

    def __init__(self,library):
        super().__init__()
        self.resize(800, 600)
        self.library = library

        layout_principale = QVBoxLayout()          #container 
        layout_info = QVBoxLayout()
        layout_count = QVBoxLayout()

        welcome_label = QLabel("Welcome !")
        layout_info.addWidget(welcome_label)

        #   @@@@@@@@@@@@@@@@@@      message      @@@@@@@@@@@@@@@@@@@@@@
        information_label = QLabel("This application allows you to manage: ")
        book_label = QLabel("✔ Books")
        user_label = QLabel("✔ Users")
        loan_label = QLabel("✔ Loan")

        layout_info.addWidget(information_label)
        layout_info.addWidget(book_label)
        layout_info.addWidget(user_label)
        layout_info.addWidget(loan_label)

        layout_principale.addLayout(layout_info)

        #   @@@@@@@@@@@@@@@@@@      counting      @@@@@@@@@@@@@@@@@@@@@@

        self.book_count = len(self.library.list_books())
        book_count_label = QLabel(f"📚 Books : {self.book_count}")
        
        self.user_count = len(self.library.list_users())
        user_count_label = QLabel(f"👤 Users : {self.user_count}")

        self.loans_count = len(self.library.list_loans())
        loan_count_label = QLabel(f"📖 Borrowed books : {self.loans_count}")

        layout_count.addWidget(book_count_label)
        layout_count.addWidget(user_count_label)
        layout_count.addWidget(loan_count_label)

        layout_principale.addLayout(layout_count)

        self.setLayout(layout_principale)