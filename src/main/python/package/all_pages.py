from PySide2 import QtWidgets

from package.influencer_page import InfluencerPage
from package.selections_page import SelectionsPage
from package.templates_page import TemplatesPage


class AllPages(QtWidgets.QStackedWidget) :
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

    def create_widgets(self) :
        self.influencer_page = InfluencerPage(ctx=self.ctx)
        self.selections_page = SelectionsPage(ctx=self.ctx, width=self.w, height=self.h)
        self.templates_page = TemplatesPage(ctx=self.ctx)

    def modify_widgets(self) :
        pass

    def create_layouts(self) :
        pass

    def add_widgets_to_layouts(self) :
        self.addWidget(self.influencer_page)
        self.addWidget(self.selections_page)
        self.addWidget(self.templates_page)

    def setup_connections(self) :
        pass

    # END UI


