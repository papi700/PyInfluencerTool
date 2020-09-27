from PySide2 import QtWidgets, QtGui

from package.create_template_tab import CreateTemplateTab


class TemplatesPage(QtWidgets.QWidget) :
    def __init__(self, ctx) :
        super().__init__()
        self.ctx = ctx
        self.setup_ui()

    def setup_ui(self) :
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self) :
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setObjectName("main_frame")
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)
        shadow.setOffset(2.5, -4)
        shadow.setColor(QtGui.QColor("black"))
        print(shadow.xOffset(), shadow.yOffset())
        self.tabs = QtWidgets.QTabWidget()
        # self.tabs.setGraphicsEffect(shadow)
        # self.tabs.tabBar().setGraphicsEffect(shadow)
        self.create_template_tab = CreateTemplateTab(ctx=self.ctx)
        self.tabs.addTab(self.create_template_tab, "Create template")
        self.tabs.tabBar().setGraphicsEffect(shadow)

    def modify_widgets(self) :
        css_file = self.ctx.get_resource("templates_page.css")
        with open(css_file, "r") as f :
            self.setStyleSheet(f.read())

    def create_layouts(self) :
        self.main_layout = QtWidgets.QGridLayout(self)
        self.main_layout.setMargin(0)
        self.main_frame_layout = QtWidgets.QGridLayout(self.main_frame)
        self.main_frame_layout.setMargin(0)

    def add_widgets_to_layouts(self) :
        self.main_layout.addWidget(self.main_frame, 0, 0)
        self.main_frame_layout.addWidget(self.tabs, 0, 0)
        shadow = QtWidgets.QGraphicsDropShadowEffect()

    def setup_connections(self) :
        pass
