#!/usr/bin/python3
import os
import json
import shutil
import requests
from datetime import date

current_date = date.today().strftime("%d-%m-%Y")
tdisk = shutil.disk_usage("/")[2] // (2**30)
tfiles = len(next(os.walk("/etc"))[2])
payload = {'current_date': current_date, 'api_version': 'v1', 'tdisk': tdisk, 'tfiles': tfiles}

r = requests.post('http://test.bar/test.php', data=payload)
 
with open("/tmp/response.json", mode='w', encoding='utf_8') as responceLog:
 json.dump(r.json(), responceLog)

#tezt
