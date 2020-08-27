from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Qt

try :
    from package.api.influencer import get_available_countries, get_all_influencers
    from package.api.selection import Selection
except :
    pass


class Worker(QtCore.QObject) :
    def __init__(self, followers_range, rate_range, countries, with_email_address, contacted_by) :
        super().__init__()

    def get_selection(self, name) :
        self.selection_name = name
        self.selection = Selection(name=self.selection_name, followers_range=followers_range,
                                   engagement_rate_range=rate_range, countries=countries,
                                   with_email_address=with_email_address,
                                   contacted_by=contacted_by)

    def get_number_of_selected_influencers(self) :
        return self.selection.lenght


class CreateSelectionTab(QtWidgets.QWidget) :
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
        self.followers_frame = QtWidgets.QFrame()
        self.followers_frame.setObjectName("followers_frame")

        self.followers_label = QtWidgets.QLabel("Followers number range")
        self.followers_label.setObjectName("followers_label")
        self.followers_label.setFrameShape(QtWidgets.QFrame.Box)

        self.followers_slider_frame = QtWidgets.QFrame()
        self.followers_slider_frame.setObjectName("followers_slider_frame")

        self.min_followers_slider = QtWidgets.QSlider(Qt.Horizontal, parent=self.followers_slider_frame)
        self.min_followers_slider.setGeometry(0, 0, 120, 26)
        self.min_followers_slider.setMinimum(5)
        self.min_followers_slider.setMaximum(200)
        self.min_followers_slider.setValue(5)

        self.max_followers_slider = QtWidgets.QSlider(Qt.Horizontal, parent=self.followers_slider_frame)
        self.max_followers_slider.setGeometry(150, 0, 120, 26)
        self.max_followers_slider.setMinimum(5)
        self.max_followers_slider.setMaximum(200)
        self.max_followers_slider.setValue(200)
        self.max_followers_slider.setObjectName("max_followers_slider")

        self.min_followers = "5"
        self.min_followers_label = QtWidgets.QLabel(f"Min: {self.min_followers}k", parent=self.followers_slider_frame)
        self.min_followers_label.setGeometry(0, 30, 90, 26)
        self.min_followers_label.setFrameShape(QtWidgets.QFrame.Box)

        self.max_followers = "200"
        self.max_followers_label = QtWidgets.QLabel(f"Max: {self.max_followers}k", parent=self.followers_slider_frame)
        self.max_followers_label.setGeometry(210, 30, 90, 26)
        self.max_followers_label.setFrameShape(QtWidgets.QFrame.Box)

        self.first_line = QtWidgets.QFrame()
        self.first_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.first_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        # FOR ENGAGEMENT RATE

        self.engagement_rate_frame = QtWidgets.QFrame()
        self.engagement_rate_frame.setObjectName("engagement_rate_frame")

        self.engagement_rate_label = QtWidgets.QLabel("Engagement rate range")
        self.engagement_rate_label.setObjectName("engagement_rate_label")
        self.engagement_rate_label.setFrameShape(QtWidgets.QFrame.Box)

        self.engagement_rate_slider_frame = QtWidgets.QFrame()
        self.engagement_rate_slider_frame.setObjectName("engagement_rate_slider_frame")

        self.min_engagement_rate_slider = QtWidgets.QSlider(Qt.Horizontal, parent=self.engagement_rate_slider_frame)
        self.min_engagement_rate_slider.setGeometry(0, 0, 120, 26)
        self.min_engagement_rate_slider.setMinimum(1)
        self.min_engagement_rate_slider.setMaximum(100)
        self.min_engagement_rate_slider.setValue(1)

        self.max_engagement_rate_slider = QtWidgets.QSlider(Qt.Horizontal, parent=self.engagement_rate_slider_frame)
        self.max_engagement_rate_slider.setGeometry(150, 0, 120, 26)
        self.max_engagement_rate_slider.setMinimum(1)
        self.max_engagement_rate_slider.setMaximum(100)
        self.max_engagement_rate_slider.setValue(100)

        self.min_engagement_rate = "1"
        self.min_engagement_rate_label = QtWidgets.QLabel(f"Min: {self.min_engagement_rate}%",
                                                          parent=self.engagement_rate_slider_frame)
        self.min_engagement_rate_label.setGeometry(0, 30, 90, 26)
        self.min_engagement_rate_label.setFrameShape(QtWidgets.QFrame.Box)
        self.min_engagement_rate_label.setFrameShape(QtWidgets.QFrame.Box)

        self.max_engagement_rate = "100"
        self.max_engagement_rate_label = QtWidgets.QLabel(f"Max: {self.max_engagement_rate}%",
                                                          parent=self.engagement_rate_slider_frame)
        self.max_engagement_rate_label.setGeometry(210, 30, 90, 26)
        self.max_engagement_rate_label.setFrameShape(QtWidgets.QFrame.Box)

        self.second_line = QtWidgets.QFrame()
        self.second_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.second_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        # FOR THE COUNTRIES

        self.countries_frame = QtWidgets.QFrame()
        self.countries_frame.setObjectName("countries_frame")

        self.countries_label = QtWidgets.QLabel("Countries")
        self.countries_label.setObjectName("countries_label")
        self.countries_label.setFrameShape(QtWidgets.QFrame.Box)

        self.available_countries = QtWidgets.QListWidget()

        item = QtWidgets.QListWidgetItem("All")
        item.setCheckState(Qt.Checked)
        self.available_countries.addItem(item)
        try :
            for country in get_available_countries() :
                item = QtWidgets.QListWidgetItem(country)
                item.setCheckState(Qt.Unchecked)
                self.available_countries.addItem(item)
        except :
            pass

        self.third_line = QtWidgets.QFrame()
        self.third_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.third_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        # FOR WITH EMAIL ADDRESS

        self.with_email_address_frame = QtWidgets.QFrame()
        self.with_email_address_frame.setObjectName("with_email_address_frame")

        self.with_email_adress_label = QtWidgets.QLabel("With email address only")
        self.with_email_adress_label.setObjectName("with_email_address_label")

        self.yes_check_box = QtWidgets.QCheckBox("Yes")

        self.fourth_line = QtWidgets.QFrame()
        self.fourth_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.fourth_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        # FOR CONTACTED BY

        self.contacted_by_frame = QtWidgets.QFrame()
        self.contacted_by_frame.setObjectName("contacted_by_frame")

        self.contacted_by_label = QtWidgets.QLabel("Contacted by")
        self.contacted_by_label.setObjectName("contacted_by_label")

        self.not_yet_checkbox = QtWidgets.QCheckBox("Not yet")
        self.not_yet_checkbox.setCheckState(Qt.Checked)

        self.dm_checkbox = QtWidgets.QCheckBox("DM")
        self.dm_checkbox.setCheckState(Qt.Checked)

        self.email_checkbox = QtWidgets.QCheckBox("Email")
        self.email_checkbox.setCheckState(Qt.Checked)

        # VALIDATION BUTTON

        self.validation_btn = QtWidgets.QPushButton("Create selection")
        self.validation_btn.setObjectName("validation_btn")

        # NUMBER OF INFLUENCERS LABEL
        try :
            self.influencers_count = len(get_all_influencers())
            self.influencers_count_label = QtWidgets.QLabel(
                f"Selected influencers count: {str(self.influencers_count)}")
            self.influencers_count_label.setFrameShape(QtWidgets.QFrame.Box)
            self.influencers_count_label.setObjectName("influencers_count_label")
        except :
            pass

    def modify_widgets(self) :
        css_file = self.ctx.get_resource("create_selection_tab.css")
        with open(css_file, "r") as f :
            self.setStyleSheet(f.read())

    def create_layouts(self) :
        self.followers_layout = QtWidgets.QVBoxLayout(self.followers_frame)
        self.followers_layout.setMargin(30)
        self.engagement_rate_layout = QtWidgets.QVBoxLayout(self.engagement_rate_frame)
        self.engagement_rate_layout.setMargin(30)
        self.countries_layout = QtWidgets.QVBoxLayout(self.countries_frame)
        self.countries_layout.setMargin(50)
        self.with_email_adress_layout = QtWidgets.QVBoxLayout(self.with_email_address_frame)
        self.with_email_adress_layout.setMargin(50)
        self.contacted_by_layout = QtWidgets.QVBoxLayout(self.contacted_by_frame)
        self.first_layout = QtWidgets.QHBoxLayout()
        self.second_layout = QtWidgets.QHBoxLayout()
        self.third_layout = QtWidgets.QHBoxLayout()
        self.last_layout = QtWidgets.QHBoxLayout()
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addLayout(self.first_layout)

    def add_widgets_to_layouts(self) :
        self.followers_layout.addWidget(self.followers_label)
        self.followers_layout.addWidget(self.followers_slider_frame)
        self.first_layout.addWidget(self.followers_frame)
        self.first_layout.addWidget(self.first_line)
        self.engagement_rate_layout.addWidget(self.engagement_rate_label)
        self.engagement_rate_layout.addWidget(self.engagement_rate_slider_frame)
        self.first_layout.addWidget(self.engagement_rate_frame)

        self.main_layout.addWidget(self.second_line)

        self.countries_layout.addWidget(self.countries_label)
        self.countries_layout.addWidget(self.available_countries)
        self.second_layout.addWidget(self.countries_frame)
        self.second_layout.addWidget(self.third_line)
        self.with_email_adress_layout.addWidget(self.with_email_adress_label)
        self.with_email_adress_layout.addWidget(self.yes_check_box)
        self.second_layout.addWidget(self.with_email_address_frame)
        self.main_layout.addLayout(self.second_layout)

        self.main_layout.addWidget(self.fourth_line)

        self.contacted_by_layout.addWidget(self.contacted_by_label)
        self.contacted_by_layout.addWidget(self.not_yet_checkbox)
        self.contacted_by_layout.addWidget(self.dm_checkbox)
        self.contacted_by_layout.addWidget(self.email_checkbox)
        self.third_layout.addWidget(self.contacted_by_frame)
        self.main_layout.addLayout(self.third_layout)

        self.last_layout.addWidget(self.validation_btn)
        try :
            self.last_layout.addWidget(self.influencers_count_label)
        except :
            pass
        self.main_layout.addLayout(self.last_layout)

    def setup_connections(self) :
        self.min_followers_slider.valueChanged.connect(lambda : self.get_influencers_count(self.min_followers))
        self.max_followers_slider.valueChanged.connect(lambda : self.get_influencers_count(self.max_followers))
        self.min_engagement_rate_slider.valueChanged.connect(
            lambda : self.get_influencers_count(self.min_engagement_rate))
        self.max_engagement_rate_slider.valueChanged.connect(
            lambda : self.get_influencers_count(self.max_engagement_rate))
        self.available_countries.itemChanged.connect(self.uncheck)

    # END UI

    def uncheck(self) :
        list = self.available_countries
        for i in range(1, len(get_available_countries()) + 1) :
            if list.item(0).checkState() == Qt.Checked and list.item(i).checkState() == Qt.Checked :
                list.item(0).setCheckState(Qt.Unchecked)

    def get_slider_value(self, var) :
        if var == self.min_followers:
            slider = self.min_followers_slider
            label = self.min_followers_label
            text = "Min: {}k"
        elif var == self.max_followers:
            slider = self.max_followers_slider
            label = self.max_followers_label
            text = "Max: {}k"
        elif var == self.min_engagement_rate:
            slider = self.min_engagement_rate_slider
            label = self.min_engagement_rate_label
            text = "Min: {}%"
        elif var == self.max_engagement_rate:
            slider = self.max_engagement_rate_slider
            label = self.max_engagement_rate_label
            text = "Max: {}%"
        var = slider.value()
        text = text.format(var)
        label.setText(text)
        if slider == self.max_followers_slider and slider.value() < self.min_followers_slider.value():
            self.min_followers_slider.setValue(self.max_followers_slider.value())
        elif slider == self.max_engagement_rate_slider and slider.value() < self.min_engagement_rate_slider.value():
            self.min_engagement_rate_slider.setValue(self.max_engagement_rate_slider.value())

    def get_selected_countries(self):
        list = []
        if self.available_countries.item(0).checkState() == Qt.Unchecked:
            for i in range(1, len(get_available_countries()) + 1):
                list.append(self.available_countries.item(i).text())
        else:
            list = None
        return list

    def get_influencers_count(self, var) :
        self.get_slider_value(var)
        followers_count_range = (int(str(self.min_followers)+"000"), int(str(self.max_followers)+"000"))
        engagement_rate_range = (float(self.min_engagement_rate), float(self.max_engagement_rate))
        countries = self.get_selected_countries()
        with_email = None
        if self.yes_check_box.checkState() == Qt.Checked:
            with_email = True
        contacted_by
        self.thread = QtCore.QThread()
        # self.worker = Worker()
