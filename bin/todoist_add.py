#!/usr/bin/env python3

import sys
import json
import todoist
import argparse
import config

parser = argparse.ArgumentParser(description='Add task to todoist')
parser.add_argument('-t','--task', nargs='*', help='Task Name',  required=True)
parser.add_argument('-d','--date', default="today", help='Task Due Date')
args = vars(parser.parse_args())

task = ' '.join(args['task'])
date = args['date']

api = todoist.TodoistAPI(config.todoist_api)

item = api.items.add(task, date_string=date)
api.commit()

print (task,'added', date)

