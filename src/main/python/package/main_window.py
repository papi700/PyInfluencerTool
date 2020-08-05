from PySide2 import QtWidgets

from package.navigation_menu_frame import NavigationMenuFrame
from package.all_pages import AllPages


class MainWindow(QtWidgets.QWidget) :
    def __init__(self, ctx) :
        super().__init__()
        desktop_widget = QtWidgets.QDesktopWidget()
        size = QtWidgets.QDesktopWidget.screenGeometry(desktop_widget)
        self.resize(size.width(), size.height())
        self.ctx = ctx
        self.setup_ui()

    def setup_ui(self) :
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self) :
        self.navigation_menu = NavigationMenuFrame(ctx=self.ctx)
        width = self.width() - self.navigation_menu.width()
        height = self.height()
        self.all_pages = AllPages(ctx=self.ctx, width=width, height=height)

    def modify_widgets(self) :
        css_file = self.ctx.get_resource("main.css")
        with open(css_file, "r") as f :
            self.setStyleSheet(f.read())

    def create_layouts(self) :
        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.main_layout.setMargin(0)
        self.main_layout.setSpacing(0)

    def add_widgets_to_layouts(self) :
        self.main_layout.addWidget(self.navigation_menu)
        self.main_layout.addWidget(self.all_pages)

    def setup_connections(self) :
        self.navigation_menu.influencer_page_btn.clicked.connect(
            lambda : self.go_to(self.navigation_menu.influencer_page_btn))
        self.navigation_menu.selections_page_btn.clicked.connect(
            lambda : self.go_to(self.navigation_menu.selections_page_btn))
        self.navigation_menu.templates_page_btn.clicked.connect(
            lambda : self.go_to(self.navigation_menu.templates_page_btn))

        # END UI

    def go_to(self, button) :
        buttons = [self.navigation_menu.influencer_page_btn,
                   self.navigation_menu.selections_page_btn,
                   self.navigation_menu.templates_page_btn]
        pages = [self.all_pages.influencer_page,
                 self.all_pages.selections_page,
                 self.all_pages.templates_page]
        button.setDown(True)
        for btn in buttons :
            if btn != button and btn.isDown() :
                btn.setDown(False)
        for i in range(len(buttons)):
            if buttons[i].isDown():
                self.all_pages.setCurrentWidget(pages[i])
                if self.all_pages.currentWidget() == pages[i]:
                    button.setDown(True)





