from PySide2 import QtWidgets


class InfluencerPage(QtWidgets.QWidget) :
    def __init__(self) :
        super().__init__()
        self.setup_ui()

    def setup_ui(self) :
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self) :
        self.main_frame = QtWidgets.QFrame()
        self.validation_btn = QtWidgets.QPushButton("Add datas")
        labels_value = ["username", "followers", "engagement rate", "country", "name", "mail", "contacted by",
                        "DM response time", "email response time", "deal offer", "story views",
                        "swipeup link clicks", "conversion rate", "generated turnover",
                        "generated followers"]
        self.labels = []
        self.entries = []
        i = 0
        for label in labels_value :
            self.labels.append(QtWidgets.QLabel(label))
            if label != "contacted by":
                self.entries.append(QtWidgets.QLineEdit())
            else:
                self.entries.append(QtWidgets.QComboBox())
                self.entries[i].addItem("not yet")
                self.entries[i].addItem("DM and mail")
                self.entries[i].addItem("mail only")
                self.entries[i].addItem("DM only")
            i += 1
        X = 0
        for i in range(1, 16) :
            if i == 1 or i == 6 or i == 11:
                Y = 150
                if X == 0:
                    X += 200
                else:
                    X += 270
                for counter in range(i-1, i+4):
                    self.labels[counter].setGeometry(X, Y, 100, 16)
                    self.labels[counter].setParent(self.main_frame)
                    self.entries[counter].setGeometry(X, Y+20, 250, 25)
                    self.entries[counter].setParent(self.main_frame)
                    Y += 70
        self.validation_btn.setGeometry(200, Y+20, 790, 35)
        self.validation_btn.setParent(self.main_frame)

    def modify_widgets(self) :
        pass

    def create_layouts(self) :
        self.main_layout = QtWidgets.QGridLayout(self)

    def add_widgets_to_layouts(self) :
        # pass
        # self.main_layout.addWidget(self.labels[0])
        # self.main_layout.addWidget(self.labels[1])

        self.main_layout.addWidget(self.main_frame, 0, 0)
    #     y_starting = 0
    #     x_starting = 0
    #     y_ending = 1
    #     x_ending = 1
    #     for label in self.labels:
    #         self.main_layout.addWidget(label, y_starting, x_starting, y_ending, x_ending)
    #         entry_y_starting = y_starting + 1
    #         entry_y_ending = y_ending + 1
    #         self.main_layout.addWidget(entry, entry_y_starting, x_starting, entry_y_ending, x_ending)
    #        y_starting += 1
    #        y_ending += 1

    def setup_connections(self) :
        pass
