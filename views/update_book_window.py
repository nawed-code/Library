from PySide6.QtWidgets import QWidget, QLineEdit,QVBoxLayout,QLabel,QPushButton,QMessageBox

class UpdateBookWindow(QWidget):

    def __init__(self,library):
        super().__init__()
        self.library = library

        self.setWindowTitle("Update a book")
        self.resize(500,300)

        book_id_label = QLabel("Book id :")
        book_title_label = QLabel("Book title :")
        book_author_label = QLabel("Book author :")
        book_category_label = QLabel("Book category :")
        book_year_label = QLabel("Book year :")

        self.book_id_input = QLineEdit()
        self.book_title_input = QLineEdit()
        self.book_author_input = QLineEdit()
        self.book_category_input = QLineEdit()
        self.book_year_input = QLineEdit()

        button = QPushButton("Update",self)
        button.clicked.connect(self.update_book)

        layout = QVBoxLayout()
        layout.addWidget(book_id_label)
        layout.addWidget(self.book_id_input)
        layout.addWidget(book_title_label)
        layout.addWidget(self.book_title_input)
        layout.addWidget(book_author_label)
        layout.addWidget(self.book_author_input)
        layout.addWidget(book_category_label)
        layout.addWidget(self.book_category_input)
        layout.addWidget(book_year_label)
        layout.addWidget(self.book_year_input)

        layout.addWidget(button)
        self.setLayout(layout)

    
    def update_book(self):
        try:
            book_id = int(self.book_id_input.text())
        except ValueError:
            QMessageBox.warning(self,"Error","The id must be a number")
            return 
        book_title = self.book_title_input.text()
        book_author = self.book_author_input.text()
        book_category = self.book_category_input.text()

        if( not book_title.strip() or not book_author.strip() or not book_category.strip()):
            QMessageBox.warning(self,"Error","All sections must be written")
            return
        
        try:
            book_year = int(self.book_year_input.text())
        except ValueError:
            QMessageBox.warning(self,"Error","The year must be a number")
            return 

        if self.library.update_book(book_id,book_title,book_author,book_category,book_year):
            self.library.save()
            print("Book updated successfully")
            self.close()
        else:
            QMessageBox.warning(self,"Error","This book is not in the library")
            return 