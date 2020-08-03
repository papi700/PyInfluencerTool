from PySide2 import QtWidgets

from package.navigation_menu_frame import NavigationMenuFrame
from package.all_pages import AllPages


class MainWindow(QtWidgets.QWidget) :
    def __init__(self) :
        super().__init__()
        self.setup_ui()

    def setup_ui(self) :
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self) :
        self.navigation_menu_frame = NavigationMenuFrame()
        self.all_pages = AllPages()

    def modify_widgets(self) :
        pass

    def create_layouts(self) :
        self.main_layout = QtWidgets.QGridLayout(self)

    def add_widgets_to_layouts(self) :
        self.main_layout.addWidget(self.navigation_menu_frame, 0, 0, 2, 1)
        self.main_layout.addWidget(self.all_pages, 0, 1, 2, 10)

    def setup_connections(self) :
        pass
