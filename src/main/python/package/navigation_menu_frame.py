from PySide2 import QtWidgets


class NavigationMenuFrame(QtWidgets.QFrame) :
    def __init__(self) :
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.influencer_page_btn = QtWidgets.QPushButton("Influencer")
        self.selections_page_btn = QtWidgets.QPushButton("Selections")
        self.templates_page_btn = QtWidgets.QPushButton("Templates")

    def modify_widgets(self):
        pass

    def create_layouts(self):
        self.main_layout = QtWidgets.QGridLayout(self)

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.influencer_page_btn, 0, 0, 1, 2)
        self.main_layout.addWidget(self.selections_page_btn, 1, 0, 1, 2)
        self.main_layout.addWidget(self.templates_page_btn, 2, 0, 1, 2)

    def setup_connections(self):
        pass
