#!/usr/bin/env python3

import todoist
import datetime
import config
import argparse
from os.path import expanduser
import os
import os.path

home = expanduser("~")

parser = argparse.ArgumentParser(description='Guest Preacher Todos')
parser.add_argument('-n','--name', nargs='*', help='Name',  required=True)
parser.add_argument('-d','--date', default="today", help='Date')
parser.add_argument('-o','--outside', default="yes", help='Outside Guest?')
args = vars(parser.parse_args())

name = ' '.join(args['name'])
date = args['date']
outside = args['outside']
today = datetime.date.today()

name_sliced = name.split()
slug = ("_".join(name_sliced))

def set_date(number):
    new_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    new_date = new_date + datetime.timedelta(days=number)
    return new_date

project_id=project_id = '2196468619'

# Now Add tasks to Todoist

api = todoist.TodoistAPI(config.todoist_api)

# add name to text file
pc_date = today
item = api.items.add('Add ' + name + ' as preacher in text file for '+ date, project_id=project_id, date_string=pc_date.strftime('%Y-%m-%d'))

# run bio in bulletin
fill_date = set_date(-6)
item = api.items.add('Run Bio for ' + name + ' in bulletin for this week', project_id=project_id, date_string=fill_date.strftime('%Y-%m-%d'))

# request check if outside guest
if outside in ['true', '1', 't', 'y', 'Yes', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']:
    check_date = set_date(-10)
    item = api.items.add('Request check for ' + name + ' preaching on ' + date, project_id=project_id, date_string=check_date.strftime('%Y-%m-%d'))

api.commit()
