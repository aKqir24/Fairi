from sys import argv, exit
from AddUI import AddUIConfig
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QFrame, QPushButton, QWidget, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize as BTSize, Qt
from cssutils import parseString

class UIConfig(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Just Arrange")
        self.setGeometry( 168, 164, 875, 565 )
        self.setStyleSheet("background-color: #242424")
        self.frontButtons()
        self.AddDisplayFrame()
        self.searchArrange()

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

        AddButton.move( 35, 35 )
        StartButton.move( 100, 35 )
        SettingsButton.move( 788, 35 )
        AddButton.clicked.connect(self.AddUI)
        StartButton.clicked.connect(self.AddUI)
        SettingsButton.clicked.connect(self.AddUI)

        def setButtonsStyle():
            AddButton.setStyleSheet(readStyle()[0]+readStyle()[3])
            StartButton.setStyleSheet(readStyle()[1]+readStyle()[4])
            SettingsButton.setStyleSheet(readStyle()[1]+readStyle()[4])

        return setButtonsStyle()

    def searchArrange(self):
        searchBox = QLineEdit("Search", self)
        searchBox.setGeometry( 165, 35, 550, 52 )
        searchBox.setStyleSheet(readStyle()[2]+readStyle()[5])

        searchButton = QPushButton("", self)
        searchButton.setStyleSheet(readStyle()[1]+readStyle()[4])
        searchButton.setFixedSize( 52, 52 )
        searchButton.move( 725, 35 )

    def AddDisplayFrame(self):
        Arrangements = QFrame(self)
        Arrangements.setGeometry(35, 110, 805, 425 )
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
            for index, rule in enumerate (readStyle):
                style_rules = [

                                # Stand By
                                "#add_button", "#universal_button", "#searchbox",

                                # When Hover
                                "#add_button:hover", "#universal_button:hover", "#searchbox:hover"

                              ]

                rule_type = [
                                # Stand By
                                "QPushButton", "QPushButton", "QLineEdit",

                                # When Hover
                                "QPushButton:hover", "QPushButton:hover", "QLineEdit:hover"

                            ]

                if rule.type == rule.STYLE_RULE and rule.selectorText == style_rules[index]:
                    buttonStyle = rule.cssText.replace( style_rules[index], rule_type[index])
                    button_style.append(str(buttonStyle.replace("\n", "")))
        return button_style

    program = QApplication(argv)
    interface = UIConfig()
    interface.show()
    exit(program.exec_())
