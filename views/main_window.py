from PySide6.QtWidgets import QWidget

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("Library Management")
        self.resize(800, 600)