from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QFrame, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize as BTSize, Qt

class AddUIConfig(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Your Arrangement")
        self.setGeometry( 168, 164, 538, 655 )

    def directoryDialog():
        pass

class UIConfig(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Just Arrange")
        self.setGeometry( 168, 164, 870, 560 )
        self.setStyleSheet("background-color: #242424")
        self.frontButtons()
        self.AddDisplayFrame()

    def frontButtons(self):
        AddButton = QPushButton("", self)
        StartButton = QPushButton("", self)
        SettingsButton = QPushButton("", self)
        AddButton.setFixedSize(52,52)
        StartButton.setFixedSize(52,52)
        SettingsButton.setFixedSize(52,52)

        AddButton.setIcon(QIcon("UI_icons\\add.svg"))
        StartButton.setIcon(QIcon("UI_icons\\play_arrow.svg"))
        SettingsButton.setIcon(QIcon("UI_icons\\settings.svg"))
        AddButton.setIconSize(BTSize(40, 40))
        StartButton.setIconSize(BTSize(40, 40))
        SettingsButton.setIconSize(BTSize(30, 30))

        AddButton.move( 35, 485 )
        StartButton.move( 430, 485 )
        SettingsButton.move( 788, 485 )
        AddButton.clicked.connect(self.AddUI)
        StartButton.clicked.connect(self.AddUI)
        SettingsButton.clicked.connect(self.AddUI)

        def setButtonsStyle():
            unified_button_style =  "padding: 9px 14px; border: 1px solid #434343;"
            individual_button_style = [ "background-color: #008170; border:1px solid #008170",
                                        "background-color: #434343;",
                                        "background-color: #434343;" ]
            AddButton.setStyleSheet(unified_button_style+individual_button_style[0])
            StartButton.setStyleSheet(unified_button_style+individual_button_style[1])
            SettingsButton.setStyleSheet(unified_button_style+individual_button_style[2])

        return setButtonsStyle()

    def AddDisplayFrame(self):
        Arrangements = QFrame(self)
        Arrangements.setGeometry(35, 35, 805, 425 )
        Arrangements.setStyleSheet("background: #303030")

    def AddUI(self):
        self.interface = AddUIConfig()
        self.interface.show()

    def SettingsUI(self):
        #TODO: Make A Setting For Icons In buttons With Test or not
        pass

if __name__ == '__main__':
    program = QApplication(argv)
    interface = UIConfig()
    interface.show()
    exit(program.exec_())
