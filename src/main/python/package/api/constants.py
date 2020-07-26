import os
from pathlib import Path


scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

cred = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(cred)

sheet = client.open("test").sheet1

SELECTIONS_DIR = os.path.join(Path.home(), ".selections")
