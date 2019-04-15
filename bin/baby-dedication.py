#!/usr/bin/env python3

import todoist
import datetime
import config
import argparse
from os.path import expanduser
import os
import os.path

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

home = expanduser("~")

parser = argparse.ArgumentParser(description='Set up Baby Dedication Template')
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

project_id = '155478376'

api = todoist.TodoistAPI(config.todoist_api)

# make baby dedication certificate
certificate_date = set_date(-4)
item = api.items.add('Print ' + name + ' dedication certificate ' + date, project_id, date_string=certificate_date.strftime('%Y-%m-%d'))

# make baby dedication certificate
pc_date = set_date(-15)
item = api.items.add('Add ' + name + ' dedication in Planning Center ' + date, project_id, date_string=pc_date.strftime('%Y-%m-%d'))
api.commit()

# Compile baby dedication certificate
dedication_date = datetime.datetime.strptime(date, '%Y-%m-%d') 
day = dedication_date.strftime('%d')
day = custom_strftime('{S}', dedication_date)
month = dedication_date.strftime('%B')
year = dedication_date.strftime('%Y')

filename =(home + '/Dropbox/Administration/Certificates/Baby_Dedication/Dedications/' + date + "_" + slug + '.md')

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

os.system('pandoc ' + filename + ' -o ~/Print/' + date + '_' + slug + '.pdf --pdf-engine=xelatex --template=baby_dedication.tex')

