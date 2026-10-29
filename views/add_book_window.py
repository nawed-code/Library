from PySide6.QtWidgets import QWidget, QLineEdit,QVBoxLayout,QLabel,QPushButton
from models.book import Book



class AddBookWindow(QWidget):

    def __init__(self,library):
        super().__init__()
        self.library = library
        self.setWindowTitle("Add a book")
        self.resize(400,300)

        self.title_input = QLineEdit()
        self.author_input = QLineEdit()
        self.category_input = QLineEdit()
        self.year_input = QLineEdit()

        title_label = QLabel("Title")
        author_label = QLabel("Author")
        category_label = QLabel("Category")
        year_label = QLabel("Year")

        layout = QVBoxLayout()
        layout.addWidget(title_label)
        layout.addWidget(self.title_input)

        layout.addWidget(author_label)
        layout.addWidget(self.author_input)

        layout.addWidget(category_label)
        layout.addWidget(self.category_input)

        layout.addWidget(year_label)
        layout.addWidget(self.year_input)

        button = QPushButton("Save",self)
        layout.addWidget(button)
        button.clicked.connect(self.save_book)

        self.setLayout(layout)

    def save_book(self):

        title = self.title_input.text()
        author = self.author_input.text()
        category = self.category_input.text()
        try:
            year = int(self.year_input.text())
        except ValueError:
            print("The year must be a number")
            return
        
        id = len(self.library.list_books())+1
        book = Book(id,title,author,category,year,True)
        
        self.library.add_book(book)
        self.library.save()
        print("book added")