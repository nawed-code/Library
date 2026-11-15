from PySide6.QtWidgets import QWidget, QLineEdit,QVBoxLayout,QLabel,QPushButton,QMessageBox,QHBoxLayout,QTabWidget

class HomeTab(QWidget):

    def __init__(self,library):
        super().__init__()
        self.resize(800, 600)
        self.library = library
        