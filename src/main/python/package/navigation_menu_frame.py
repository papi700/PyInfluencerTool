from PySide2 import QtWidgets


class NavigationMenuFrame(QtWidgets.QFrame) :
    def __init__(self, ctx) :
        super().__init__()
        self.ctx = ctx
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()

    def create_widgets(self):
        self.influencer_page_btn = QtWidgets.QPushButton("Influencer")
        self.selections_page_btn = QtWidgets.QPushButton("Selections")
        self.templates_page_btn = QtWidgets.QPushButton("Templates")

    def modify_widgets(self):
        css_file = self.ctx.get_resource("navigation_menu_frame.css")
        with open(css_file, "r") as f :
            self.setStyleSheet(f.read())

    def create_layouts(self):
        self.main_layout = QtWidgets.QGridLayout(self)
        self.main_layout.setMargin(0)
        self.main_layout.setSpacing(0)

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.influencer_page_btn)
        self.main_layout.addWidget(self.selections_page_btn)
        self.main_layout.addWidget(self.templates_page_btn)


