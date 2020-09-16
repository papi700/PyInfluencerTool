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
        self.selection_information = QtWidgets.QGroupBox("Selection information")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.selection_information.setFont(font)
        self.selections_list.setMaximumHeight(200)
        self.selections_list.setMaximumWidth(1271)
        self.selection_information.setMaximumWidth(1271)

        self.criteria_label = QtWidgets.QLabel("Criterias:")
        self.criteria_label.setObjectName("criteria_label")
        self.criteria_label.setFrameShape(QtWidgets.QFrame.Box)

        self.creation_date_label = QtWidgets.QLabel("Creation date:")
        self.creation_date_label.setObjectName("creation_date_label")
        self.creation_date_label.setFrameShape(QtWidgets.QFrame.Box)

        self.criterias_label = QtWidgets.QLabel()
        self.criterias_label.setObjectName("criterias_label")
        self.criterias_label.setWordWrap(True)
        self.criterias_label.setFrameShape(QtWidgets.QFrame.Box)

    def modify_widgets(self) :
        css_file = self.ctx.get_resource("my_selections_tab.css")
        with open(css_file, "r") as f :
            self.setStyleSheet(f.read())

    def create_layouts(self) :
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.selection_information_layout = QtWidgets.QGridLayout(self.selection_information)

    def add_widgets_to_layouts(self) :
        self.main_layout.addWidget(self.selections_list)
        self.main_layout.addWidget(self.selection_information)
        self.selection_information_layout.addWidget(self.criteria_label, 0, 0, 1, 1)
        self.selection_information_layout.addWidget(self.creation_date_label, 0, 1, 1, 1)
        self.selection_information_layout.addWidget(self.criterias_label, 1, 0, 2, 2)

    def setup_connections(self) :
        self.selections_list.itemSelectionChanged.connect(self.show_selection_information)

    # END UI

    def add_selection_to_listwidget(self, selection) :
        lw_item = QtWidgets.QListWidgetItem(selection.name)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        lw_item.selection = selection
        lw_item.setFont(font)
        self.selections_list.addItem(lw_item)

    def populate_selections(self) :
        selections = get_selections()
        for selection in selections :
            self.add_selection_to_listwidget(selection)

    def turn_list_into_string(self, list) :
        items_str = list[0]
        for item in list :
            if item != list[len(list) - 1] and item != list[len(list) - 2] :
                items_str += item + ", "
            elif item == list[len(list) - 2] :
                items_str += item + "and "
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
                followers_range_str = "{0}-{1}".format(str(followers_range[0]).replace("000", "K"),
                                                       str(followers_range[1]).replace("000", "K"))
                followers_range_str = "followers: " + followers_range_str + "\n"
                all_criterias.append(followers_range_str)
            if selection.engagement_rate_range :
                engagement_rate_range = selection.engagement_rate_range
                engagement_rate_range_str = str(engagement_rate_range[0]) + "%" + "-" + str(
                    engagement_rate_range[1]) + "%"
                engagement_rate_range_str = "engagement rate: " + engagement_rate_range_str + "\n"
                all_criterias.append(engagement_rate_range_str)
            countries = selection.countries
            if countries and len(countries) > 1 :
                print(selection.countries)
                countries_str = self.turn_list_into_string(countries)
                countries_str = "countries: " + countries_str + "\n"
                all_criterias.append(countries_str)
            elif countries and len(countries) == 1 :
                print(selection.countries)
                all_criterias.append("country: " + selection.countries[0] + "\n")
            if selection.with_email_address :
                all_criterias.append("with email address \n")
            contacted_by = selection.contacted_by
            if contacted_by and len(contacted_by) > 1 :
                contacted_by_str = self.turn_list_into_string(contacted_by)
                contacted_by_str = "contacted by: " + contacted_by_str + "\n"
            elif contacted_by and len(contacted_by) == 1 :
                all_criterias.append("contacted by: " + contacted_by + "\n")

            for criteria in all_criterias :
                self.criterias_label.setText(self.criterias_label.text() + criteria)
