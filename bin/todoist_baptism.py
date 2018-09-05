#!/usr/bin/env python3

import sys
import json
import todoist
import time
import datetime
import config
import sys
import subprocess
import urltools
import argparse

parser = argparse.ArgumentParser(description='Set up Baptism Template')
parser.add_argument('-n','--name', nargs='*', help='Name',  required=True)
parser.add_argument('-d','--date', default="today", help='Date of Baptism')
args = vars(parser.parse_args())


name = ' '.join(args['name'])
date = args['date']
today = datetime.date.today()

project_id = '155477514'

# Now Add tasks to Todoist

api = todoist.TodoistAPI(config.todoist_api)

# add to planning center
pc_date = today
item = api.items.add('Add ' + name + ' baptism to planning center', project_id, date_string=pc_date.strftime('%Y-%m-%d'))

# contact Larry about filling baptistry
fill_date = datetime.datetime.strptime(date, '%Y-%m-%d') 
fill_date = fill_date + datetime.timedelta(days=-6)
item = api.items.add('Contact Larry to fill baptistry for ' + name + ' baptism', project_id, date_string=fill_date.strftime('%Y-%m-%d'))
api.commit()

# double check baptistry
check_date = datetime.datetime.strptime(date, '%Y-%m-%d') 
check_date = check_date + datetime.timedelta(days=-1)
item = api.items.add('Make sure baptistry is filled for ' + name + ' baptism', project_id, date_string=check_date.strftime('%Y-%m-%d'))
api.commit()

# make baptism certificate
certificate_date = datetime.datetime.strptime(date, '%Y-%m-%d') 
certificate_date = certificate_date + datetime.timedelta(days=-4)
item = api.items.add('Make ' + name + ' baptism certificate', project_id, date_string=certificate_date.strftime('%Y-%m-%d'))
api.commit()

# add baptism date to database
database_date = datetime.datetime.strptime(date, '%Y-%m-%d') 
database_date = database_date + datetime.timedelta(days=+1)
item = api.items.add('Add ' + name + ' baptism information to database', project_id, date_string=database_date.strftime('%Y-%m-%d'))
api.commit()

# email_address = 'clif@fbcmuncie.org'
# subject = 'Baptism on {}'.format(date.strftime('%B %d, %Y'))
# message = ('Hi Clif%0A%0AI just wanted you to know that {} is going to be baptized on {}. I have added it to planning center.%0A%0AWade'.format(name, date.strftime('%B %d, %Y')))
# url = 'https://mail.google.com/mail/?view=cm&fs=1&to=' + email_address + '&su=' + subject + '&body=' + message
# subprocess.call(["xdg-open", url])

