from PySide2 import QtWidgets

from package.create_selection_tab import CreateSelectionTab


class SelectionsPage(QtWidgets.QWidget) :
    def __init__(self, ctx, width=0, height=0) :
        super().__init__()
        self.ctx = ctx
        self.w = width
        self.h = height
        self.setup_ui()

    def setup_ui(self) :
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.tabs = QtWidgets.QTabWidget(self)
        self.create_selection_tab = CreateSelectionTab(ctx=self.ctx)
        self.tabs.addTab(self.create_selection_tab, "Create selection")

    def modify_widgets(self) :
        css_file = self.ctx.get_resource("selections_page.css")
        with open(css_file, "r") as f :
            self.setStyleSheet(f.read())

    def create_layouts(self) :
        pass

    def add_widgets_to_layouts(self) :
        pass

    def setup_connections(self) :
        pass
