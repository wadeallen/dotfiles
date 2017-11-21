#!/usr/bin/env python3

import sys
import json
import todoist
from dateutil import parser
import time
import datetime
import config

name = input("Name of person: ")
date = input("Date of Funeral: ")
church = input("Is the funeral at the church? (y/n): ")

date = parser.parse(date)

today = parser.parse(time.strftime("%m %d %Y"))
# add to funeral project
project_id = '162548698'

# Now Add tasks to Todoist

api = todoist.TodoistAPI(config.todoist_api)

# sets the notify church about death
notify_date = today
item = api.items.add('email congregation about ' + name + ' death and funeral arrangements', project_id, date_string=notify_date.strftime('%Y-%m-%d'))

# meet with family
item = api.items.add('Set up meeting with ' + name + ' family', project_id, date_string=notify_date.strftime('%Y-%m-%d'))

# mark deceased in database
item = api.items.add('mark ' + name + ' deceased in database', project_id, date_string=notify_date.strftime('%Y-%m-%d'))

# print backup copy of funeral
print_backup = date + datetime.timedelta(days=-1)
item = api.items.add('print backup copy of funeral sermon for ' + name + ' funeral', project_id, date_string=print_backup.strftime('%Y-%m-%d'))

if church in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']:
    # check and add to church calendar
    item = api.items.add('check calendar and add funeral for ' + name + ' to calendar', project_id, date_string=notify_date.strftime('%Y-%m-%d'))
    # line up sound tech
    item = api.items.add('line up sound tech for ' + name + ' funeral', project_id, date_string=notify_date.strftime('%Y-%m-%d'))
    # notify Adam
    item = api.items.add('notify Adam or Clif about moving sounds equipment for ' + name + ' funeral', project_id, date_string=notify_date.strftime('%Y-%m-%d'))


api.commit()

print ('Funeral Added:',name,date.strftime('%B %d, %Y'))
