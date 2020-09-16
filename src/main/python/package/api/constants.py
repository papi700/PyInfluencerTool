from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os
import re
from pathlib import Path

try :
    SCOPE = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    CRED = ServiceAccountCredentials.from_json_keyfile_name("D:/PythonProjects/creds.json", SCOPE)

    CLIENT = gspread.authorize(CRED)

    SHEET = CLIENT.open("test").sheet1
except :
    pass

SERVER_LOGIN = os.environ.get('SERVER_LOGIN')

SERVER_PASSWORD = os.environ.get('SERVER_PASSWORD')

SELECTIONS_DIR = os.path.join(Path.home(), ".selections")

TEMPLATES_DIR = os.path.join(Path.home(), ".templates")

TEMPLATES_VARIABLES = ["username", "followers", "engagement rate", "country", "name", "mail"]

TEMPLATES_VARIABLES_REGEX = r'\[([^\]]+)\]'
