class AddProperties(AddUIConfig):
    def __init__(self):
        super().__init__()
        self.add_button.clicked.connect(self.source_folders)

    def extensions(self):
        pass

    def source_folders(self):
        selected = QFileDialog.getExistingDirectory(self, 'Add source folders:')

    def keywords():
        pass

    def indiacate():
        pass
