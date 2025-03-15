from Start_ import QWidget, QLabel, BTSize, Qt

class AddUIConfig(QWidget):
    def __init__(self, STYLES):
        super().__init__()
        self.setWindowTitle("Add Your Arrangement")
        self.setStyleSheet("background-color: #242424")
        self.setGeometry( 295, 155, 538, 645 )
        self.directoryDialog(STYLES)

    def directoryDialog(self, STYLES):
        # TODO: Make A Label With Settings For The Arrangements
        tooltip_style = STYLES['Labels_Txt'][1].replace("QLabel:hover", "QToolTip")
        tooltip_txt = " In What Folder To Put Your Arranged Files!!"
        dir_txt_label = QLabel("Folder Directory:", self)
        dir_txt_label.setStyleSheet(STYLES['Labels_Txt'][0]+tooltip_style)
        dir_txt_label.setToolTip(tooltip_txt)
        dir_txt_label.move(25, 25)

class AddFunctions:
    def Extensions():
        pass

    def OutputFolder():
        pass

    def KeyWord():
        pass

    def indiacate():
        pass
