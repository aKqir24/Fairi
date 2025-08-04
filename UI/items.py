from .dialogs import
from .parent import QWidget, QLabel, BTSize, Qt, QPushButton, QVBoxLayout

class AddUIConfig(QWidget):
    def __init__(self, STYLES):
        super().__init__()
        self.setWindowTitle("Add Your Arrangement")
        self.setStyleSheet("background-color: #242424")
        self.setGeometry( 295, 155, 538, 645 )

        self.add_button = QPushButton('Add')
        self.dataSETUP(STYLES)

    def dataSETUP(self, STYLES):
        # TODO: Make A Label With Settings For The Arrangements
        source_layout = QVBoxLayout()
        tooltip_style = STYLES['Labels_Txt'][1].replace("QLabel:hover", "QToolTip")
        tooltip_txt = " In What Folder To Put Your Arranged Files!!"
        
        source_label = QLabel("Sources:", self)
        source_label.setStyleSheet(STYLES['Labels_Txt'][0]+tooltip_style)
        source_label.setToolTip(tooltip_txt)
        source_label.move(25, 25)
        
        source_layout.addWidget(self.add_button)
        self.setLayout(source_layout)


