from sys import argv, exit
from Add_UI import AddUIConfig
from Settings_UI import SettingsUIConfig
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
        self.searchArrange()

    #? TopLevel Windows
    def openAddUI(self):
        self.add_ui = AddUIConfig()
        self.add_ui.show()

    def openSettingsUI(self):
        #TODO: Make A Setting For Icons In buttons With Test or not
        self.settings_ui = SettingsUIConfig()
        self.settings_ui.show()

    #? Button Setups
    def frontButtons(self):
        AddButton = QPushButton("", self)
        StartButton = QPushButton("", self)
        SettingsButton = QPushButton("", self)
        AddButton.setFixedSize(52,52)
        StartButton.setFixedSize(52,52)
        SettingsButton.setFixedSize(52,52)

        def setButtonsConfig():
            #? Icons
            AddButton.setIcon(QIcon("UI_icons\\add.svg"))
            StartButton.setIcon(QIcon("UI_icons\\play_arrow.svg"))
            SettingsButton.setIcon(QIcon("UI_icons\\settings.svg"))
            AddButton.setIconSize(BTSize(40, 40))
            StartButton.setIconSize(BTSize(40, 40))
            SettingsButton.setIconSize(BTSize(30, 30))

            #? Stylesheet
            AddButton.setStyleSheet(readStyle()[0]+readStyle()[3])
            StartButton.setStyleSheet(readStyle()[1]+readStyle()[4])
            SettingsButton.setStyleSheet(readStyle()[1]+readStyle()[4])

            #? Position
            AddButton.move( 35, 35 )
            StartButton.move( 100, 35 )
            SettingsButton.move( 788, 35 )

            #? Commands
            AddButton.clicked.connect(self.openAddUI)
            StartButton.clicked.connect(self.openSettingsUI)
            SettingsButton.clicked.connect(self.openSettingsUI)

        return setButtonsConfig()

    def searchArrange(self):
        searchBox = QLineEdit("", self)
        searchBox.setPlaceholderText("Search...")
        searchBox.setGeometry( 165, 35, 550, 52 )
        searchBox.setStyleSheet(readStyle()[2]+readStyle()[5])

        searchButton = QPushButton("", self)
        searchButton.setStyleSheet(readStyle()[1]+readStyle()[4])
        searchButton.setFixedSize( 52, 52 )
        searchButton.move( 725, 35 )

if __name__ == '__main__':
    def readStyle():
        button_style = []
        with open('UI_styles.css', 'r') as styleFile:
            readStyle = parseString(styleFile.read())
            for index, rule in enumerate (readStyle):
                style_rules = { 'Css-Ids': [ "#add_button", "#universal_button", "#searchbox" ],
                                'Qt-Ids': [ "QPushButton", "QPushButton", "QLineEdit" ] }

                if index < int(len(style_rules['Css-Ids'])):
                    if rule.type == rule.STYLE_RULE and rule.selectorText == style_rules['Css-Ids'][index]:
                        buttonStyle = rule.cssText.replace(style_rules['Css-Ids'][index], style_rules['Qt-Ids'][index])
                        button_style.append(str(buttonStyle.replace("\n", "")))

                else:
                    if rule.type == rule.STYLE_RULE and rule.selectorText == style_rules['Css-Ids'][index-3]+":hover":
                        buttonStyle_hover = rule.cssText.replace(style_rules['Css-Ids'][index-3]+":hover", style_rules['Qt-Ids'][index-3]+":hover")
                        button_style.append(str(buttonStyle_hover.replace("\n", "")))

        return button_style

    program = QApplication(argv)
    interface = UIConfig()
    interface.show()
    exit(program.exec_())
