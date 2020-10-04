from glob import glob
from uuid import uuid4
import json
import os
import re

from package.api.constants import TEMPLATES_DIR, TEMPLATES_VARIABLES, TEMPLATES_VARIABLES_REGEX


def get_templates():
    templates = []
    files = glob(os.path.join(TEMPLATES_DIR, "*.json"))
    for file in files:
        with open(file, "r") as f:
            template_data = json.load(f)
            template_type = template_data.get("type")
            template_name = template_data.get("name")
            template_uuid = template_data.get("uuid")
            if template_type == "email":
                template_subject = template_data.get("subject")
                template_body = template_data.get("body")
                template = EmailTemplate(type=template_type, name=template_name, uuid=template_uuid,
                                         subject=template_subject, body=template_body)
                templates.append(template)
            else:
                # template_content = template_data.get("content")
                # template = DMTemplate(type=template_type, name=template_name, uuid=template_uuid,
                # content=template_subject)
                pass
            templates.append(template)
    return templates


class EmailTemplate:
    def __init__(self, type="", name="", uuid="", subject="", body=""):
        self.type = "email"
        if name == "":
            directory_lenght = len(glob(os.path.join(TEMPLATES_DIR, "*.json")))
            self.name = "template_" + str(directory_lenght + 1)
        else:
            self.name = name
        if uuid == "":
            self.uuid = str(uuid4())
        else:
            self.uuid = uuid
        self.subject = subject
        self.body = body

    def check_variables(self):
        invalid_variables = []
        matching_list = []
        pattern = re.compile(TEMPLATES_VARIABLES_REGEX)
        subject_matches = pattern.finditer(self.subject)
        body_matches = pattern.finditer(self.body)
        for match in subject_matches:
            matching_list.append((match, "subject"))
        for match in body_matches:
            matching_list.append((match, "body"))
        for match_and_place in matching_list:
            if match_and_place[0].group(1) not in TEMPLATES_VARIABLES:
                invalid_variables.append((match_and_place[0].group(1), match_and_place[1]))
            if match_and_place == matching_list[len(matching_list) - 1]:
                if invalid_variables == []:
                    return True
                else:
                    return invalid_variables

    def get_variables(self):
        variables = []
        if self.check_variables() == True:
            pattern = re.compile(TEMPLATES_VARIABLES_REGEX)
            subject_matches = pattern.finditer(self.subject)
            body_matches = pattern.finditer(self.body)
            for match in subject_matches:
                if not match in variables:
                    variables.append((match.group(0), "subject"))
            for match in body_matches:
                if not match in variables:
                    variables.append((match.group(0), "body"))
            return variables
        else:
            return False

    def replace_variables_in(self, place, values):
        if place == "subject":
            text = self.subject
        else:
            text = self.body
        variables = self.get_variables()
        variables_and_keys = [("[username]", 0), ("[followers]", 1), ("[engagement rate]", 2), ("[country]", 3),
                              ("[name]", 4), ("[mail]", 5)]
        if variables:
            place_variables = []
            for variable in variables:
                if variable[1] == place:
                    place_variables.append(variable[0])
            for variable in place_variables:
                for i in range(len(variables_and_keys)):
                    if variable == variables_and_keys[i][0]:
                        text = text.replace(variable, values[variables_and_keys[i][1]])
        return text

    @property
    def path(self):
        return os.path.join(TEMPLATES_DIR, self.uuid + ".json")

    def save(self):
        if not os.path.exists(TEMPLATES_DIR):
            os.makedirs(TEMPLATES_DIR)
        data = {"type": self.type, "name": self.name,
                "subject": self.subject,
                "body": self.body}
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)


class DMTemplate:
    pass


if __name__ == '__main__':
    # subject = "Let’s build something together! [username] + Vlowny"
    body = """
    Hi [username],

I’m Seny from Vlowny. We’re dreaming up a new product, and we’ve been hoping to partner with an influencer who wants to help us develop it and make it their own.

I’ve been following your Instagram and I think you’d be a perfect fit.

Here’s how the process would work:

    We are going to create a discount code to the name of your instagram account.
    We will send you a picture of the product we want you to promote.
    You will make a swipe up story with that picture.
    You will receive 0.5$ every time your code is used, which represents 500$ for 1000 sales with your code
    Do you have some time this week to chat about what this partnership could look like?

Look forward to hearing from you,

Seny 
"""
    # t = Email_template(subject=subject, body=body)
    # t.save()
    # print(get_templates())
