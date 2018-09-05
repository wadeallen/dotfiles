#!/usr/bin/env python3

import todoist
import datetime
import config
import argparse
from os.path import expanduser
import os
import os.path
from datetime import datetime as dt

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

home = expanduser("~")

parser = argparse.ArgumentParser(description='Set up Baptism Template')
parser.add_argument('-n','--name', nargs='*', help='Name',  required=True)
parser.add_argument('-d','--date', default="today", help='Date of Baptism')
args = vars(parser.parse_args())

name = ' '.join(args['name'])
date = args['date']
today = datetime.date.today()

name_sliced = name.split()
slug = ("_".join(name_sliced))

def set_date(number):
    new_date = datetime.datetime.strptime(date, '%Y-%m-%d') 
    new_date = new_date + datetime.timedelta(days=number)
    return new_date

project_id = '155477514'

# Now Add tasks to Todoist

api = todoist.TodoistAPI(config.todoist_api)

# add to planning center
pc_date = today
item = api.items.add('Add ' + name + ' baptism to planning center', project_id, date_string=pc_date.strftime('%Y-%m-%d'))

# contact Larry about filling baptistry
fill_date = set_date(-6)
item = api.items.add('Contact Larry to fill baptistry for ' + name + ' baptism', project_id, date_string=fill_date.strftime('%Y-%m-%d'))

# double check baptistry
check_date = set_date(-1)
item = api.items.add('Make sure baptistry is filled for ' + name + ' baptism', project_id, date_string=check_date.strftime('%Y-%m-%d'))

make baptism certificate
certificate_date = set_date(-4)
item = api.items.add('Make ' + name + ' baptism certificate', project_id, date_string=certificate_date.strftime('%Y-%m-%d'))

# add baptism date to database
database_date = set_date(+1)
item = api.items.add('Add ' + name + ' baptism information to database', project_id, date_string=database_date.strftime('%Y-%m-%d'))
# api.commit()

baptism_date = datetime.datetime.strptime(date, '%Y-%m-%d') 
day = baptism_date.strftime('%d')
day = custom_strftime('{S}', baptism_date)
month = baptism_date.strftime('%B')
year = baptism_date.strftime('%Y')

filename =(home + '/Dropbox/Administration/Certificates/Baptism/Baptisms/' + date + "_" + slug + '.md')

if os.path.isfile(filename):
	print("File already exists")
else:
    target = open (filename, 'w')
    target.write("---\n")
    target.write("name: " + name + "\n")
    target.write("day: " + day + "\n")
    target.write("month: " + month + "\n")
    target.write("year: " + year + "\n")
    target.write("---\n")
    target.close()

os.system('pandoc ' + filename + ' -o ~/Dropbox/Print/' + date + '_' + slug + '.pdf --latex-engine=xelatex --template=baptism.tex')

