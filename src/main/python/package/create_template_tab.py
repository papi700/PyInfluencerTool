from PySide2 import QtWidgets

import re

from package.api.template import EmailTemplate

class CreateTemplateTab(QtWidgets.QWidget) :
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
        self.subject_frame = QtWidgets.QFrame()
        self.subject_label = QtWidgets.QLabel("Subject: ")
        self.subject_input = QtWidgets.QLineEdit()
        self.body_input = QtWidgets.QTextEdit()
        self.create_btn = QtWidgets.QPushButton("Create")

    def modify_widgets(self):
        css_file = self.ctx.get_resource("create_template_tab.css")
        with open(css_file, "r") as f :
            self.setStyleSheet(f.read())

    def create_layouts(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.subject_layout = QtWidgets.QHBoxLayout(self.subject_frame)

    def add_widgets_to_layouts(self):
        self.subject_layout.addWidget(self.subject_label)
        self.subject_layout.addWidget(self.subject_input)
        self.main_layout.addWidget(self.subject_frame)
        self.main_layout.addWidget(self.body_input)
        self.main_layout.addWidget(self.create_btn)

    def setup_connections(self):
        self.create_btn.clicked.connect(self.create_template)

    def show_variables(self):
        pass

    def create_template(self):
        self.message_box = QtWidgets.QMessageBox(self)
        self.message = ""
        if self.subject_input.text() != "":
            subject = self.subject_input.text()
        else:
            subject = None

        if self.body_input != "":
            body = self.body_input.toPlainText()
        else:
            body = None

        if not subject and not body:
            self.message = "Template empty"
        elif not subject:
            self.message = "Subject empty"
        elif not body:
            self.message = "Body empty"
        elif subject and body:
            template = EmailTemplate(subject=subject, body=body)
            dialog = QtWidgets.QInputDialog(self)
            name, result = dialog.getText(self, "Ajouter une note", "Titre: ", text=template.name)
            if result:
                template.save()
                self.message = f"Template of name '{name}', created."

        self.message_box.setText(self.message)
        if self.message != "":
            self.message_box.exec_()
