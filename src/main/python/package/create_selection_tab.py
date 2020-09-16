from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Qt

try :
    from package.api.influencer import get_available_countries, get_all_influencers
    from package.api.selection import Selection
except :
    pass


class Worker(QtCore.QObject) :
    def __init__(self, obj) :
        super().__init__()
        self.obj = obj

    def uncheck(self) :
        o = self.obj
        list = o.available_countries
        for i in range(1, len(get_available_countries()) + 1) :
            if list.item(0).checkState() == Qt.Checked and list.item(i).checkState() == Qt.Checked :
                list.item(0).setCheckState(Qt.Unchecked)


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
        self.min_engagement_rate_slider.setValue(0)

        self.max_engagement_rate_slider = QtWidgets.QSlider(Qt.Horizontal, parent=self.engagement_rate_slider_frame)
        self.max_engagement_rate_slider.setGeometry(150, 0, 120, 26)
        self.max_engagement_rate_slider.setMinimum(0)
        self.max_engagement_rate_slider.setMaximum(100)
        self.max_engagement_rate_slider.setValue(100)

        self.min_engagement_rate = "0"
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

        self.dm_checkbox = QtWidgets.QCheckBox("DM only")
        self.dm_checkbox.setCheckState(Qt.Checked)

        self.email_checkbox = QtWidgets.QCheckBox("Mail only")
        self.email_checkbox.setCheckState(Qt.Checked)

        self.dm_and_email_checkbox = QtWidgets.QCheckBox("DM and mail")
        self.dm_and_email_checkbox.setCheckState(Qt.Checked)

        # CLEAR BUTTON
        self.clear_btn = QtWidgets.QPushButton("Clear")
        self.clear_btn.setObjectName("clear_btn")

        # VALIDATION BUTTON

        self.validation_btn = QtWidgets.QPushButton("Create selection")
        self.validation_btn.setObjectName("validation_btn")

        # NUMBER OF INFLUENCERS LABEL
        try :
            self.selection = Selection(followers_range=(5000, 200000), engagement_rate_range=(0, 100))
            self.influencers_count = self.selection.lenght
            self.influencers_count_label = QtWidgets.QLabel(
                f"Selected influencers count: {str(self.influencers_count)}")
            self.influencers_count_label.setFrameShape(QtWidgets.QFrame.Box)
            self.influencers_count_label.setObjectName("influencers_count_label")
        except :
            self.influencers_count_label.setText("No connection")

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
        self.contacted_by_layout.addWidget(self.dm_and_email_checkbox)
        self.third_layout.addWidget(self.contacted_by_frame)
        self.main_layout.addLayout(self.third_layout)

        self.last_layout.addWidget(self.clear_btn)

        self.last_layout.addWidget(self.validation_btn)
        try :
            self.last_layout.addWidget(self.influencers_count_label)
        except :
            pass
        self.main_layout.addLayout(self.last_layout)

    def setup_connections(self) :
        self.min_followers_slider.valueChanged.connect(lambda : self.get_influencers_count(followers=True))
        self.max_followers_slider.valueChanged.connect(lambda : self.get_influencers_count(followers=True))
        self.min_engagement_rate_slider.valueChanged.connect(lambda : self.get_influencers_count(engagement=True))
        self.max_engagement_rate_slider.valueChanged.connect(lambda : self.get_influencers_count(engagement=True))
        self.available_countries.itemChanged.connect(lambda : self.get_influencers_count(countries=True))
        self.yes_check_box.stateChanged.connect(self.get_influencers_count)
        self.dm_checkbox.stateChanged.connect(self.get_influencers_count)
        self.email_checkbox.stateChanged.connect(self.get_influencers_count)
        self.dm_and_email_checkbox.stateChanged.connect(self.get_influencers_count)
        self.clear_btn.clicked.connect(self.clear)
        self.validation_btn.clicked.connect(self.save_selection)

    # END UI

    def control_slider(self, min, max) :
        if max.value() < min.value() :
            min.setValue(max.value())

    def get_selected_countries(self) :
        list = []
        if self.available_countries.item(0).checkState() == Qt.Unchecked :
            for i in range(1, len(get_available_countries()) + 1) :
                if self.available_countries.item(i).checkState() == Qt.Checked :
                    list.append(self.available_countries.item(i).text())
        else :
            list = None
        return list

    def get_influencers_count(self, followers=None, engagement=None, countries=None) :
        if followers :
            self.control_slider(self.min_followers_slider, self.max_followers_slider)
            self.min_followers = self.min_followers_slider.value()
            self.min_followers_label.setText(f"Min: {self.min_followers}k")
            self.max_followers = self.max_followers_slider.value()
            self.max_followers_label.setText(f"Max: {self.max_followers}k")
        elif engagement :
            self.control_slider(self.min_engagement_rate_slider, self.max_engagement_rate_slider)
            self.min_engagement_rate = self.min_engagement_rate_slider.value()
            self.min_engagement_rate_label.setText(f"Min: {self.min_engagement_rate}%")
            self.max_engagement_rate = self.max_engagement_rate_slider.value()
            self.max_engagement_rate_label.setText(f"Max: {self.max_engagement_rate}%")
        elif countries :
            self.thread = QtCore.QThread(self)
            self.worker = Worker(self)
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.uncheck)
            self.thread.start()
        followers_count_range = (int(str(self.min_followers) + "000"), int(str(self.max_followers) + "000"))
        engagement_rate_range = (float(self.min_engagement_rate), float(self.max_engagement_rate))
        countries = self.get_selected_countries()
        with_email = None
        if self.yes_check_box.checkState() == Qt.Checked :
            with_email = True
        contacted_by_checkboxes = [self.not_yet_checkbox, self.dm_checkbox, self.email_checkbox,
                                   self.dm_and_email_checkbox]
        contacted_by = []
        for checkbox in contacted_by_checkboxes :
            if checkbox.checkState() == Qt.Checked and checkbox.text() == "Not yet" :
                contacted_by.append("not yet")
            elif checkbox.checkState() == Qt.Checked and checkbox.text() == "DM only" :
                contacted_by.append("DM")
            elif checkbox.checkState() == Qt.Checked and checkbox.text() == "Mail only" :
                contacted_by.append("mail only")
            elif checkbox.checkState() == Qt.Checked and checkbox.text() == "DM and mail" :
                contacted_by.append("DM and mail")
        if len(contacted_by) == 4 :
            contacted_by = None
        try :
            self.selection = Selection(followers_range=followers_count_range,
                                       engagement_rate_range=engagement_rate_range, countries=countries,
                                       with_email_address=with_email,
                                       contacted_by=contacted_by)
            self.influencers_count = self.selection.lenght
            self.influencers_count_label.setText(f"Selected influencers count: {str(self.influencers_count)}")
        except :
            pass

    def clear(self) :
        self.min_followers_slider.setValue(5)
        self.max_followers_slider.setValue(200)
        self.min_engagement_rate_slider.setValue(0)
        self.max_engagement_rate_slider.setValue(100)
        self.available_countries.item(0).setCheckState(Qt.Checked)
        for i in range(1, len(get_available_countries()) + 1) :
            self.available_countries.item(i).setCheckState(Qt.Unchecked)
        self.yes_check_box.setCheckState(Qt.Unchecked)
        self.not_yet_checkbox.setCheckState(Qt.Checked)
        self.dm_checkbox.setCheckState(Qt.Checked)
        self.email_checkbox.setCheckState(Qt.Checked)
        self.dm_and_email_checkbox.setCheckState(Qt.Checked)

    def save_selection(self) :
        self.dialog = QtWidgets.QDialog(self)
        self.dialog.setWindowTitle("Create Selection")
        dialog_main_layout = QtWidgets.QVBoxLayout(self.dialog)
        dialog_H_layout_1 = QtWidgets.QHBoxLayout()
        dialog_H_layout_2 = QtWidgets.QHBoxLayout()
        selection_name_label = QtWidgets.QLabel("Selection name: ")
        selection_name_label.setObjectName("selection_name_label")
        selection_name_label.setFrameShape(QtWidgets.QFrame.Box)

        edit = QtWidgets.QLineEdit(self.selection.name)

        dialog_H_layout_1.addWidget(selection_name_label)
        dialog_H_layout_1.addWidget(edit)

        buttons_frame = QtWidgets.QFrame()
        buttons_frame.setObjectName("buttons_frame")
        button_1 = QtWidgets.QPushButton("Ok")
        button_1.setObjectName("button_1")
        button_2 = QtWidgets.QPushButton("Cancel")
        button_2.setObjectName("button_2")

        ok_btn = QtWidgets.QDialogButtonBox(parent=buttons_frame)
        ok_btn.setGeometry(150, 0, 80, 30)
        ok_btn.addButton(button_1, QtWidgets.QDialogButtonBox.AcceptRole)
        ok_btn.accepted.connect(self.dialog.accept)

        cancel_btn = QtWidgets.QDialogButtonBox(parent=buttons_frame)
        cancel_btn.setGeometry(245, 0, 80, 30)
        cancel_btn.addButton(button_2, QtWidgets.QDialogButtonBox.RejectRole)
        cancel_btn.rejected.connect(self.dialog.reject)

        dialog_H_layout_2.addWidget(buttons_frame)

        dialog_main_layout.addLayout(dialog_H_layout_1)
        dialog_main_layout.addLayout(dialog_H_layout_2)

        def save(obj) :
            try :
                obj.selection.save()
                message_box = QtWidgets.QMessageBox(obj)
                message_box.setText(f"Selection of name '{edit.text()}', created.")
                message_box.show()
            except :
                pass

        self.dialog.accepted.connect(lambda : save(self))

        self.dialog.exec_()
