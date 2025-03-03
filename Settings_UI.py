from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QSize as BTSize, Qt

class SettingsUIConfig(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setStyleSheet("background-color: #242424")
        self.setGeometry( 295, 164, 625, 565 )

    def directoryDialog():
        # TODO: Make A Label With Settings For The Arrangements
        pass
