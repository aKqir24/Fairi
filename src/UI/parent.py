from .icons import parent_icon
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize as BTSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QFrame, QPushButton, QWidget, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout

class UIConfig(QMainWindow):
    def __init__(self, STYLE_OWNER):
        super().__init__()
        self.STYLES = STYLE_OWNER
        self.center_widget = QWidget()
        self.setCentralWidget(self.center_widget)
        self.widgets_wrapper = QVBoxLayout(self.center_widget)
        self.setWindowTitle("Just Arrange")
        self.setGeometry( 168, 164, 875, 565 )
        self.setStyleSheet("QMainWindow"+self.STYLES['UI_BG'])
        self.frontWidgets( STYLE_OWNER, self.searchArrange(STYLE_OWNER),
                           self.addArrangeFrame() )

    #? Open TopLevel Windows
    def openAddUI(self):
        from .items import AddUIConfig
        self.add_ui = AddUIConfig(self.STYLES)
        self.add_ui.show()

    def openSettingsUI(self):
        #TODO: Make A Setting For Icons In buttons With Test or not
        from .settings import SettingsUIConfig
        self.settings_ui = SettingsUIConfig(self.STYLES)
        self.settings_ui.show()

    #? Button Setups
    def frontWidgets(self, STYLES, searchArea, arrangeFrame):
        AddButton = QPushButton("", self)
        StartButton = QPushButton("", self)
        SettingsButton = QPushButton("", self)
        AddButton.setMinimumSize(42,42)
        StartButton.setMinimumSize(42,42)
        SettingsButton.setMinimumSize(60,60)
        searchButton, searchBox = searchArea

        def setButtonsConfig(): 
            #? Icons
            AddButton.setIcon(QIcon(f"{parent_icon[0]}"))
            StartButton.setIcon(QIcon(f"{parent_icon[1]}"))
            SettingsButton.setIcon(QIcon(f"{parent_icon[2]}"))
            AddButton.setIconSize(BTSize(40, 40))
            StartButton.setIconSize(BTSize(40, 40))
            SettingsButton.setIconSize(BTSize(30, 30))

            #? Stylesheet
            AddButton.setStyleSheet(STYLES['Add_BT'])
            StartButton.setStyleSheet(STYLES['Default_BT'])
            SettingsButton.setStyleSheet(STYLES['Default_BT'])

            #? Commands
            AddButton.clicked.connect(self.openAddUI)
            StartButton.clicked.connect(self.openSettingsUI)
            SettingsButton.clicked.connect(self.openSettingsUI)

            def addToLayout():
                widgets_container = QHBoxLayout()
                widgets_container.setSpacing(8)
                for widget in \
                    [ AddButton, StartButton, searchBox, searchButton, SettingsButton ]:
                    widgets_container.addWidget(widget)
 
                widgets_container.setContentsMargins( 0, 0, 0, 8 )
                self.widgets_wrapper.addLayout(widgets_container)
                self.widgets_wrapper.setContentsMargins( 25, 25, 25, 25 )
                self.widgets_wrapper.addWidget(arrangeFrame)

            return addToLayout()
        return setButtonsConfig()

    def searchArrange(self, STYLES):
        searchBox = QLineEdit("", self)
        searchBox.setPlaceholderText("Search...")
        searchBox.setStyleSheet(STYLES['Search_Box'])
        searchBox.setMinimumHeight( 60 )

        searchButton = QPushButton("", self)
        searchButton.setIcon(QIcon(f"{parent_icon[3]}"))
        searchButton.setStyleSheet(STYLES['Search_BT'])
        searchButton.setIconSize(BTSize(35, 35))
        searchButton.setMinimumSize( 60, 60 )
        searchButton.move( 725, 35 )
        searchButton.clicked.connect( lambda : print(searchBox.text()) )
        return (searchButton, searchBox)

    def addArrangeFrame(self):
        arrange_container = QFrame()
        arrange_container.setMinimumSize(10,10)
        arrange_container.setStyleSheet("background-color: #2F2F2F")
        return arrange_container

def initiateMainUI(STYLE_OWNER):
    from sys import argv, exit
    program = QApplication(argv)
    interface = UIConfig(STYLE_OWNER)
    interface.show()
    exit(program.exec_())
