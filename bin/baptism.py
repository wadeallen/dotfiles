#!/usr/bin/env python3

import datetime
from os.path import expanduser
import os
import os.path
import todoist
import argparse
import config
from titlecase import titlecase

home = expanduser("~")

parser = argparse.ArgumentParser(description='Set up Baptism')
parser.add_argument('-n','--name', nargs='*', help='Name',  required=True)
parser.add_argument('-d','--date', default="today", help='Date of Baptism')
parser.add_argument('-i','--immersion', default="yes", help='Is the baptism immersion?')
args = vars(parser.parse_args())

name = ' '.join(args['name'])
# name = input("Name: ")
name = titlecase(name)
date = args['date']
today = datetime.date.today()
# date = input("Date: ")
full_name = name
first_name = name.split()[0].capitalize()


name_sliced = name.split()
slug = ("_".join(name_sliced))

def set_date(number):
    new_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    new_date = new_date + datetime.timedelta(days=number)
    new_date = new_date.strftime('%Y-%m-%d')
    return new_date

today = today.strftime('%Y-%m-%d')
# add to baptism project
project_id = '2269381711'

# Now Add tasks to Todoist

api = todoist.TodoistAPI(config.todoist_api)

#function to add item
def addTodo(days,task):
	if days == 0:
		notify_date = today
	else:
		notify_date = set_date(days)
	item = api.items.add(f"{task}: {name} baptism", project_id=project_id, date_string=notify_date)

addTodo(0,"notify Carolyn")
addTodo(0,"get approval from OB")
addTodo(-1,"bring clothes")
addTodo(-5,"contact Ed about filling tank")
addTodo(-5, "email or text reminder to candidate")

api.commit()

