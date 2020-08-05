from PySide2 import QtWidgets


class TemplatesPage(QtWidgets.QWidget) :
    def __init__(self, ctx) :
        super().__init__()
        self.ctx = ctx
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        pass

    def modify_widgets(self):
        css_file = self.ctx.get_resource("templates_page.css")
        with open(css_file, "r") as f :
            self.setStyleSheet(f.read())

    def create_layouts(self):
        pass

    def add_widgets_to_layouts(self):
        pass

    def setup_connections(self):
        pass
