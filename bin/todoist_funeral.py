#!/usr/local/bin/python3

import sys
import json
import todoist
from dateutil import parser
import time
import datetime
import config

# Breaks the string down to separate arguments

name = input("Name of Deceased: ")
date = input("Date of Funeral: ")

date = parser.parse(date)

today = parser.parse(time.strftime("%m %d"))
project_id = '162548698'

# Now Add tasks to Todoist

api = todoist.TodoistAPI(config.todoist_api)

# sets the notify date
notify_date = today
item = api.items.add('Notify Clif about clearing stage for ' + name + ' funeral', project_id, date_string=notify_date.strftime('%Y-%m-%d'))
item = api.items.add('Call Betty or Nina about funeral dinner for ' + name + ' funeral', project_id, date_string=notify_date.strftime('%Y-%m-%d'))
item = api.items.add('Email Church about ' + name + ' passing away', project_id, date_string=notify_date.strftime('%Y-%m-%d'))
item = api.items.add('Schedule time to meet with ' + name + ' family', project_id, date_string=notify_date.strftime('%Y-%m-%d'))
item = api.items.add('Add ' + name + ' funeral and visitation to calendar', project_id, date_string=notify_date.strftime('%Y-%m-%d'))
item = api.items.add('Work on  ' + name + ' funeral', project_id, date_string=notify_date.strftime('%Y-%m-%d'))

api.commit()

print ('Funeral Added:',name,date.strftime('%B %d, %Y'))
