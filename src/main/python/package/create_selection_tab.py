from PySide2 import QtWidgets
from PySide2.QtCore import Qt

import re

try :
    from package.api.influencer import get_available_countries
    from package.api.sheet import in_int
except :
    pass


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

        self.min_followers_frame = QtWidgets.QFrame()

        self.max_followers_frame = QtWidgets.QFrame()

        self.min_followers_label = QtWidgets.QLabel("Min", parent=self.min_followers_frame)
        self.min_followers_label.setGeometry(0, 0, 70, 26)
        self.min_followers_label.setFrameShape(QtWidgets.QFrame.Box)

        self.min_followers_entry = QtWidgets.QLineEdit("5K", parent=self.min_followers_frame)
        self.min_followers_entry.setGeometry(80, 0, 180, 35)

        self.max_followers_label = QtWidgets.QLabel("Max", parent=self.max_followers_frame)
        self.max_followers_label.setGeometry(0, 0, 70, 26)
        self.max_followers_label.setFrameShape(QtWidgets.QFrame.Box)

        self.max_followers_entry = QtWidgets.QLineEdit("200m", parent=self.max_followers_frame)
        self.max_followers_entry.setGeometry(80, 0, 180, 35)

        self.first_line = QtWidgets.QFrame()
        self.first_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.first_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        # FOR ENGAGEMENT RATE

        self.engagement_rate_frame = QtWidgets.QFrame()
        self.engagement_rate_frame.setObjectName("engagement_rate_frame")

        self.engagement_rate_label = QtWidgets.QLabel("Engagement rate range")
        self.engagement_rate_label.setObjectName("engagement_rate_label")
        self.engagement_rate_label.setFrameShape(QtWidgets.QFrame.Box)

        self.min_engagement_rate_frame = QtWidgets.QFrame()

        self.max_engagement_rate_frame = QtWidgets.QFrame()

        self.min_engagement_rate_label = QtWidgets.QLabel("Min", parent=self.min_engagement_rate_frame)
        self.min_engagement_rate_label.setGeometry(0, 0, 70, 26)
        self.min_engagement_rate_label.setFrameShape(QtWidgets.QFrame.Box)

        self.min_engagement_rate_entry = QtWidgets.QLineEdit("0%", parent=self.min_engagement_rate_frame)
        self.min_engagement_rate_entry.setGeometry(80, 0, 180, 35)

        self.max_engagement_rate_label = QtWidgets.QLabel("Max", parent=self.max_engagement_rate_frame)
        self.max_engagement_rate_label.setGeometry(0, 0, 70, 26)
        self.max_engagement_rate_label.setFrameShape(QtWidgets.QFrame.Box)

        self.max_engagement_rate_entry = QtWidgets.QLineEdit("100%", parent=self.max_engagement_rate_frame)
        self.max_engagement_rate_entry.setGeometry(80, 0, 180, 35)

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

        for country in get_available_countries() :
            item = QtWidgets.QListWidgetItem(country)
            item.setCheckState(Qt.Unchecked)
            self.available_countries.addItem(item)

        self.third_line = QtWidgets.QFrame()
        self.third_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.third_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        # FOR WITH EMAIL ADDRESS

        self.with_email_address_frame = QtWidgets.QFrame()
        self.with_email_address_frame.setObjectName("with_email_address_frame")

        self.with_email_adress_label = QtWidgets.QLabel("With email address")
        self.with_email_adress_label.setObjectName("with_email_address_label")

        self.yes_radio_btn = QtWidgets.QRadioButton("Yes")
        self.no_radio_btn = QtWidgets.QRadioButton("No")

        self.fourth_line = QtWidgets.QFrame()
        self.fourth_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.fourth_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        # FOR CONTACTED BY

        self.contacted_by_frame = QtWidgets.QFrame()
        self.contacted_by_frame.setObjectName("contacted_by_frame")

        self.contacted_by_label = QtWidgets.QLabel("Contacted by")
        self.contacted_by_label.setObjectName("contacted_by_label")

        self.not_yet_checkbox = QtWidgets.QCheckBox("Not yet")

        self.dm_checkbox = QtWidgets.QCheckBox("DM")

        self.email_checkbox = QtWidgets.QCheckBox("Email")

        # VALIDATION BUTTON

        self.validation_btn = QtWidgets.QPushButton("Create selection")
        self.validation_btn.setObjectName("validation_btn")

        # NUMBER OF INFLUENCERS LABEL

        self.influencers_number = 0
        self.influencers_number_label = QtWidgets.QLabel(f"Selected influencers: {str(self.influencers_number)}")
        self.influencers_number_label.setFrameShape(QtWidgets.QFrame.Box)
        self.influencers_number_label.setObjectName("influencers_number_label")

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
        self.followers_layout.addWidget(self.min_followers_frame)
        self.followers_layout.addWidget(self.max_followers_frame)
        self.first_layout.addWidget(self.followers_frame)
        self.first_layout.addWidget(self.first_line)
        self.engagement_rate_layout.addWidget(self.engagement_rate_label)
        self.engagement_rate_layout.addWidget(self.min_engagement_rate_frame)
        self.engagement_rate_layout.addWidget(self.max_engagement_rate_frame)
        self.first_layout.addWidget(self.engagement_rate_frame)

        self.main_layout.addWidget(self.second_line)

        self.countries_layout.addWidget(self.countries_label)
        self.countries_layout.addWidget(self.available_countries)
        self.second_layout.addWidget(self.countries_frame)
        self.second_layout.addWidget(self.third_line)
        self.with_email_adress_layout.addWidget(self.with_email_adress_label)
        self.with_email_adress_layout.addWidget(self.yes_radio_btn)
        self.with_email_adress_layout.addWidget(self.no_radio_btn)
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
        self.last_layout.addWidget(self.influencers_number_label)

        self.main_layout.addLayout(self.last_layout)

    def setup_connections(self) :
        self.validation_btn.clicked.connect(self.check_QLineEdit)

    # END UI

    def check_QLineEdit(self) :
        min_followers_match = re.match(r"^\d+(\.\d+)?[kKmM]{1}$", self.min_followers_entry.text())
        max_followers_match = re.match(r"^\d+(\.\d+)?[kKmM]{1}$", self.max_followers_entry.text())
        min_engagement_rate_match = re.match(r"^\d+(\.\d+)?%?$", self.min_engagement_rate_entry.text())
        max_engagement_rate_match = re.match(r"^\d+(\.\d+)?%?$", self.max_engagement_rate_entry.text())
        regex = False
        check = False
        self.message_box = QtWidgets.QMessageBox()
        if self.min_followers_entry.text() != "5k" and not min_followers_match :
            self.message_box.setText("Please enter a valid minimum followers number eg. 2.1k")
            self.message_box.setIcon(QtWidgets.QMessageBox.Critical)
        elif self.max_followers_entry.text() != "200m" and not max_followers_match :
            self.message_box.setText("Please enter a valid maximum followers number eg. 2.1k")
            self.message_box.setIcon(QtWidgets.QMessageBox.Critical)
        elif self.min_engagement_rate_entry.text() != "0%" and not min_engagement_rate_match :
            self.message_box.setText("Please enter a valid minimum engament rate eg. 2.1% or 2.1")
            self.message_box.setIcon(QtWidgets.QMessageBox.Critical)
        elif self.max_engagement_rate_entry.text() != "100%" and not max_engagement_rate_match :
            self.message_box.setText("Please enter a valid maximum engament rate eg. 2.1% or 2.1")
            self.message_box.setIcon(QtWidgets.QMessageBox.Critical)
        else :
            regex = True
        if regex :
            min_followers = self.min_followers_entry.text()
            max_followers = self.max_followers_entry.text()
            if "%" in self.min_engagement_rate_entry.text() :
                min_engagement = self.min_engagement_rate_entry.text().replace("%", "")
            else :
                min_engagement = self.min_engagement_rate_entry.text()
            if "%" in self.max_engagement_rate_entry.text() :
                max_engagement = self.max_engagement_rate_entry.text().replace("%", "")
            else :
                max_engagement = self.max_engagement_rate_entry.text()
            if in_int(min_followers) >= in_int(max_followers) :
                self.message_box.setText("The minimum followers number should be always smaller than the maximum")
            elif float(min_engagement) >= float(max_engagement) :
                self.message_box.setText("The minimum engagement rate should be always smaller than the maximum")
            else :
                check = True
        if check :
            return True
        else:
            self.message_box.exec_()
