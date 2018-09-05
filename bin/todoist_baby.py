#!/usr/bin/env python3

import sys
import json
import todoist
import time
import datetime
import config
import argparse

parser = argparse.ArgumentParser(description='Set up Baby Dedication Template')
parser.add_argument('-n','--name', nargs='*', help='Name',  required=True)
parser.add_argument('-d','--date', default="today", help='Date of Baptism')
args = vars(parser.parse_args())

name = ' '.join(args['name'])
date = args['date']
today = datetime.date.today()

def set_date(number):
    new_date = datetime.datetime.strptime(date, '%Y-%m-%d') 
    new_date = new_date + datetime.timedelta(days=number)
    return new_date

project_id = '155478376'

api = todoist.TodoistAPI(config.todoist_api)

# make baby dedication certificate
certificate_date = set_date(-4)
item = api.items.add('Make ' + name + ' dedication certificate ' + date, project_id, date_string=certificate_date.strftime('%Y-%m-%d'))

# make baby dedication certificate
pc_date = set_date(-15)
item = api.items.add('Add ' + name + ' dedication in Planning Center ' + date, project_id, date_string=pc_date.strftime('%Y-%m-%d'))
api.commit()

