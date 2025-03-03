from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QSize as BTSize, Qt

class AddUIConfig(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Your Arrangement")
        self.setStyleSheet("background-color: #242424")
        self.setGeometry( 295, 155, 538, 645 )

    def directoryDialog():
        # TODO: Make A Label With Settings For The Arrangements
        pass
