import re
from PySide2 import QtWidgets
import google.auth.exceptions

try:
    from package.api.influencer import EmailError
except:
    pass

from package.api.selection import get_selections


class InfluencerPage(QtWidgets.QWidget) :
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
        self.message_box = QtWidgets.QMessageBox()
        self.main_frame = QtWidgets.QFrame()
        self.validation_btn = QtWidgets.QPushButton("Add datas")
        labels_value = ["Username", "Followers", "Engagement rate", "Country", "Name", "Mail", "Contacted by",
                        "DM response time", "Email response time", "Deal offer", "Story views",
                        "Swipeup link clicks", "Conversion rate", "Generated turnover",
                        "Generated followers"]
        self.labels = []
        self.entries = []
        i = 0
        for label in labels_value :
            self.labels.append(QtWidgets.QLabel(label))
            if label != "Contacted by" :
                self.entries.append(QtWidgets.QLineEdit())
            else :
                self.entries.append(QtWidgets.QComboBox())
                self.entries[i].addItem("not yet")
                self.entries[i].addItem("DM and mail")
                self.entries[i].addItem("mail only")
                self.entries[i].addItem("DM only")
            i += 1
        X = 0
        for i in range(1, 16) :
            if i == 1 or i == 6 or i == 11 :
                Y = 150
                if X == 0 :
                    X += 200
                else :
                    X += 270
                for counter in range(i - 1, i + 4) :
                    self.labels[counter].setGeometry(X, Y, 200, 26)
                    self.labels[counter].setParent(self.main_frame)
                    self.entries[counter].setGeometry(X, Y + 30, 250, 30)
                    self.entries[counter].setParent(self.main_frame)
                    Y += 100
        self.validation_btn.setGeometry(200, Y + 20, 790, 35)
        self.validation_btn.setParent(self.main_frame)

    def modify_widgets(self) :
        css_file = self.ctx.get_resource("influencer_page.css")
        with open(css_file, "r") as f :
            self.setStyleSheet(f.read())

    def create_layouts(self) :
        self.main_layout = QtWidgets.QGridLayout(self)
        self.main_layout.setMargin(0)

    def add_widgets_to_layouts(self) :
        self.main_layout.addWidget(self.main_frame, 0, 0)

    def setup_connections(self) :
        self.validation_btn.clicked.connect(self.add_influencer_datas)

    # END UI

    def add_influencer_datas(self) :
        pattern = r"^(?!.*\.\.)(?!.*\.$)[^\W][\w.]{0,29}$"
        resultat = re.match(pattern, self.entries[0].text())
        if resultat :
            datas = []
            permission = None
            followers_match = re.match(r"^\d+(\.\d+)?[kKmM]{1}$", self.entries[1].text())
            engagement_rate_match = re.match(r"^\d+(\.\d+)?%?$", self.entries[2].text())
            country_match = re.match(r"(^[A-Z]{2,}-?\s?[a-z]?\s?)", self.entries[3].text())
            name_match = re.match(r"(^[A-Z]{1}([A-Z]{1,})?[a-z]+\s?)", self.entries[4].text())
            email_match = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", self.entries[5].text())
            if self.entries[1].text() != "" and not followers_match :
                self.entries[1].setStyleSheet("color: red;")
                permission = False
                self.message_box.setText("Please enter a valid followers number eg. 2.1k")
                self.message_box.setIcon(QtWidgets.QMessageBox.Critical)
            elif self.entries[2].text() != "" and not engagement_rate_match :
                permission = False
                self.entries[2].setStyleSheet("color: red;")
                self.message_box.setText("Please enter a valid engament rate eg. 2.1% or 2.1")
                self.message_box.setIcon(QtWidgets.QMessageBox.Critical)
            elif self.entries[2].text() != "" and engagement_rate_match and not "%" in self.entries[2].text() :
                self.entries[2].setText(self.entries[2].text() + "%")
                permission = True
            elif self.entries[3].text() != "" and not country_match :
                permission = False
                self.entries[3].setStyleSheet("color: red;")
                self.message_box.setText("""Please enter a valid country name.e.g:
                                              -USA
                                              -United
                                              -Ame-rica""")
                self.message_box.setIcon(QtWidgets.QMessageBox.Critical)
            elif self.entries[4].text() != "" and not name_match :
                permission = False
                self.entries[4].setStyleSheet("color: red;")
                self.message_box.setText("Please enter a valid name. Make sure that the first letter of any word of the"
                                         "name is uppercase and the rest of the word is lowercase.")
                self.message_box.setIcon(QtWidgets.QMessageBox.Critical)
            elif self.entries[5].text() != "" and not email_match :
                permission = False
                self.entries[5].setStyleSheet("color: red;")
                self.message_box.setText("Please enter a valid email address")
                self.message_box.setIcon(QtWidgets.QMessageBox.Critical)
            else :
                permission = True
                for entry in self.entries:
                    entry.setStyleSheet("color: rgb(80, 127, 230)")
            for data in self.entries :
                if permission :
                    if not isinstance(data, QtWidgets.QComboBox) :
                        datas.append(data.text())
                    else :
                        datas.append(data.currentText())
            if datas != [] :
                try :
                    from package.api.influencer import Influencer
                    i = Influencer(datas)
                    result = i.add_datas()
                    for selection in get_selections():
                        selection.update(i)
                    if result :
                        self.message_box.setText("The datas have been added to the spreadsheet")
                    else :
                        self.message_box.setText("Datas are already in the spreadsheet")
                    self.message_box.setIcon(QtWidgets.QMessageBox.Information)
                except google.auth.exceptions.TransportError :
                    self.message_box.setText("WIFI problem")
                    self.message_box.setIcon(QtWidgets.QMessageBox.Critical)
                except EmailError :
                    self.message_box.setText("This email address is not available")
                    self.message_box.setIcon(QtWidgets.QMessageBox.Information)
        else :
            self.message_box.setText("Unvalid username")
            self.message_box.setIcon(QtWidgets.QMessageBox.Critical)
        self.message_box.exec_()
