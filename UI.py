from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QFrame, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize as BTSize, Qt
from cssutils import parseString

class AddUIConfig(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Your Arrangement")
        self.setStyleSheet("background-color: #242424")
        self.setGeometry( 168, 164, 538, 655 )

    def directoryDialog():
        # TODO: Make A Label With Settings For The Arrangements
        pass

class UIConfig(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Just Arrange")
        self.setGeometry( 168, 164, 875, 560 )
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
            AddButton.setStyleSheet(readStyle()[0])
            StartButton.setStyleSheet(readStyle()[1])
            SettingsButton.setStyleSheet(readStyle()[2])

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
    def readStyle():
        button_style = []
        with open('UI_styles.css', 'r') as styleFile:
            readStyle = parseString(styleFile.read())
            for rule in readStyle:
                if rule.type == rule.STYLE_RULE and rule.selectorText == "#individual_button_0":
                    buttonStyle = rule.cssText.replace("#individual_button_0", "QPushButton")
                if rule.type == rule.STYLE_RULE and rule.selectorText == "#individual_button_1":
                    buttonStyle = rule.cssText.replace("#individual_button_1", "QPushButton")
                if rule.type == rule.STYLE_RULE and rule.selectorText == "#individual_button_2":
                    buttonStyle = rule.cssText.replace("#individual_button_2", "QPushButton")
                button_style.append(buttonStyle.replace("\n", ""))
        return button_style

    program = QApplication(argv)
    interface = UIConfig()
    interface.show()
    exit(program.exec_())
