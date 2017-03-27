#!/usr/bin/env python3

import sys
import json
import todoist
from dateutil import parser
import time
import datetime
import config


baby_name = input("Name of Baby: ")
date = input("Date of Dedication: ")

date = parser.parse(date)

project_id = '155478376'

api = todoist.TodoistAPI(config.todoist_api)

# sets the notify date
notify_date = date + datetime.timedelta(days=-6)
item = api.items.add('Notify Clif and Dana ' + baby_name + ' dedication ' + date.strftime('%Y-%m-%d'), project_id, date_string=notify_date.strftime('%Y-%m-%d'))

# make baby dedication certificate
certificate_date = date + datetime.timedelta(days=-4)
item = api.items.add('Make ' + baby_name + ' dedication certificate ' + date.strftime('%Y-%m-%d'), project_id, date_string=certificate_date.strftime('%Y-%m-%d'))
api.commit()

# make baby dedication certificate
pc_date = date + datetime.timedelta(days=-15)
item = api.items.add('Add ' + baby_name + ' dedication in Planning Center' + date.strftime('%Y-%m-%d'), project_id, date_string=pc_date.strftime('%Y-%m-%d'))
api.commit()

print ('Tasks Added:', baby_name + ' Dedication added for', date.strftime('%B %d, %Y'))
