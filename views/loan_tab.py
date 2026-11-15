from PySide6.QtWidgets import QWidget, QLineEdit,QVBoxLayout,QLabel,QPushButton,QMessageBox,QHBoxLayout,QTabWidget
from models.book import Book

class LoanTab(QWidget):

    def __init__(self,library):
        super().__init__()

        self.setWindowTitle("Loan Management")
        self.resize(800, 600)
        self.library = library
