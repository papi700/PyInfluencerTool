import re
from PySide2 import QtWidgets, QtCore, QtGui

from package.api.selection import get_selections


class MySelectionTab(QtWidgets.QWidget) :
    def __init__(self, ctx) :
        super().__init__()
        self.ctx = ctx
        self.setup_ui()
        self.populate_selections()

    def setup_ui(self) :
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self) :
        self.selections_list = QtWidgets.QListWidget()
        self.selections_list.setMaximumHeight(200)
        self.selections_list.setMaximumWidth(1271)

        self.selection_information = QtWidgets.QFrame()
        self.selection_information.setObjectName("selection_information")
        self.selection_information.setMaximumWidth(1271)

        self.criteria_label = QtWidgets.QLabel("Criterias:", parent=self.selection_information)
        self.criteria_label.setObjectName("criteria_label")
        self.criteria_label.setFrameShape(QtWidgets.QFrame.Box)
        self.criteria_label.setGeometry(0, 30, 200, 30)

        self.criterias_label = QtWidgets.QLabel(parent=self.selection_information)
        self.criterias_label.setObjectName("criterias_label")
        self.criterias_label.setWordWrap(True)
        self.criterias_label.setFrameShape(QtWidgets.QFrame.Box)
        self.criterias_label.setGeometry(20, 70, 300, 100)

        self.creation_date_label = QtWidgets.QLabel("Creation date:", parent=self.selection_information)
        self.creation_date_label.setObjectName("creation_date_label")
        self.creation_date_label.setFrameShape(QtWidgets.QFrame.Box)
        self.creation_date_label.setGeometry(0, 190, 200, 30)

        self.date_label = QtWidgets.QLabel(parent=self.selection_information)
        self.date_label.setObjectName("date_label")
        self.date_label.setFrameShape(QtWidgets.QFrame.Box)
        self.date_label.setGeometry(20, 230, 200, 30)

        self.lenght_label = QtWidgets.QLabel("Lenght:", parent=self.selection_information)
        self.lenght_label.setObjectName("lenght_label")
        self.lenght_label.setFrameShape(QtWidgets.QFrame.Box)
        self.lenght_label.setGeometry(0, 280, 200, 30)

        self.the_lenght_label = QtWidgets.QLabel(parent=self.selection_information)
        self.the_lenght_label.setObjectName("the_lenght_label")
        self.the_lenght_label.setFrameShape(QtWidgets.QFrame.Box)
        self.the_lenght_label.setGeometry(20, 320, 200, 30)

    def modify_widgets(self) :
        css_file = self.ctx.get_resource("my_selections_tab.css")
        with open(css_file, "r") as f :
            self.setStyleSheet(f.read())

    def create_layouts(self) :
        self.main_layout = QtWidgets.QVBoxLayout(self)

    def add_widgets_to_layouts(self) :
        self.main_layout.addWidget(self.selections_list)
        self.main_layout.addWidget(self.selection_information)

    def setup_connections(self) :
        self.selections_list.itemSelectionChanged.connect(self.show_selection_information)

    # END UI

    def add_selection_to_listwidget(self, selection) :
        lw_item = QtWidgets.QListWidgetItem(selection.name)
        font = QtGui.QFont()
        font.setPointSize(15)
        # font.setBold(True)
        lw_item.selection = selection
        lw_item.setFont(font)
        self.selections_list.addItem(lw_item)

    def populate_selections(self) :
        selections = get_selections()
        for selection in selections :
            self.add_selection_to_listwidget(selection)

    def turn_list_into_string(self, list) :
        items_str = ""
        for item in list :
            if item != list[len(list) - 1] and item != list[len(list) - 2] :
                items_str += item + ", "
            elif item == list[len(list) - 2] :
                items_str += item + " and "
            else :
                items_str += item
        return items_str

    def get_selected_lw_item(self) :
        selected_items = self.selections_list.selectedItems()
        if selected_items :
            return selected_items[0]
        else :
            return None

    def show_selection_information(self) :
        selected_item = self.get_selected_lw_item()
        if selected_item :
            self.criterias_label.setText("")
            all_criterias = []
            selection = selected_item.selection
            if selection.followers_range :
                followers_range = selection.followers_range
                followers_range_str = "{0}-{1}".format(re.sub("0{3}$", "K", str(followers_range[0])),
                                                       re.sub("0{3}$", "K", str(followers_range[1])))
                followers_range_str = "-Followers: " + followers_range_str + "\n"
                all_criterias.append(followers_range_str)
            if selection.engagement_rate_range :
                engagement_rate_range = selection.engagement_rate_range
                engagement_rate_range_str = str(engagement_rate_range[0]) + "%" + "-" + str(
                    engagement_rate_range[1]) + "%"
                engagement_rate_range_str = "-Engagement rate: " + engagement_rate_range_str + "\n"
                all_criterias.append(engagement_rate_range_str)
            countries = selection.countries
            if countries and len(countries) > 1 :
                countries_str = self.turn_list_into_string(countries)
                countries_str = "-Countries: " + countries_str + "\n"
                all_criterias.append(countries_str)
            elif countries and len(countries) == 1 :
                all_criterias.append("-Country: " + selection.countries[0] + "\n")
            if selection.with_email_address :
                all_criterias.append("-With email address \n")
            contacted_by = selection.contacted_by
            if contacted_by and len(contacted_by) > 1 :
                contacted_by_str = self.turn_list_into_string(contacted_by)
                contacted_by_str = "-Contacted by: " + contacted_by_str + "\n"
            elif contacted_by and len(contacted_by) == 1 :
                all_criterias.append("-Contacted by: " + contacted_by + "\n")

            for criteria in all_criterias :
                self.criterias_label.setText(self.criterias_label.text() + criteria)

            self.date_label.setText(selection.creation_date)
            self.the_lenght_label.setText(str(selection.lenght))
