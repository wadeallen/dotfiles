#!/usr/bin/env python3

import sys
import json
import todoist
from dateutil import parser
import time
import datetime
import config

name = input("Name of person: ")
date = input("Date of Baptism: ")

date = parser.parse(date)

today = parser.parse(time.strftime("%m %d %Y"))
project_id = '155477514'

# Now Add tasks to Todoist

api = todoist.TodoistAPI(config.todoist_api)

# sets the notify date
notify_date = today
item = api.items.add('Notify Clif about ' + name + ' baptism', project_id, date_string=notify_date.strftime('%Y-%m-%d'))

# add to planning center
pc_date = today
item = api.items.add('Add ' + name + ' baptism to planning center', project_id, date_string=pc_date.strftime('%Y-%m-%d'))

# contact Larry about filling baptistry
fill_date = date + datetime.timedelta(days=-6)
item = api.items.add('Contact Larry to fill baptistry for ' + name + ' baptism', project_id, date_string=fill_date.strftime('%Y-%m-%d'))
api.commit()

# double check baptistry
check_date = date + datetime.timedelta(days=-1)
item = api.items.add('Make sure baptistry is filled for ' + name + ' baptism', project_id, date_string=check_date.strftime('%Y-%m-%d'))
api.commit()

# make baby baptism certificate
certificate_date = date + datetime.timedelta(days=-4)
item = api.items.add('Make ' + name + ' baptism certificate', project_id, date_string=certificate_date.strftime('%Y-%m-%d'))
api.commit()

# add baptism date to database
database_date = date + datetime.timedelta(days=+1)
item = api.items.add('Add ' + name + ' baptism information to database', project_id, date_string=database_date.strftime('%Y-%m-%d'))
api.commit()

print ('Baptism Added:',name,date.strftime('%B %d, %Y'))
