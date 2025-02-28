from PyQt5.QtWidgets import QWidget

class AddUIConfig(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Your Arrangement")
        self.setStyleSheet("background-color: #242424")
        self.setGeometry( 168, 164, 538, 655 )

    def directoryDialog():
        # TODO: Make A Label With Settings For The Arrangements
        pass
