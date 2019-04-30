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

parser = argparse.ArgumentParser(description='Set up Funeral Template')
parser.add_argument('-n','--name', nargs='*', help='Name of Deceased',  required=True)
parser.add_argument('-d','--date', default="today", help='Date of Funeral')
parser.add_argument('-g', '--gender', default="male", help='Gender')
parser.add_argument('-c', '--church', default="yes", help='Is the funeral at the church?')
args = vars(parser.parse_args())

name = ' '.join(args['name'])
# name = input("Name of Deceased: ")
name = titlecase(name)
date = args['date']
today = datetime.date.today()
# date = input("Date of Funeral: ")
gender = args['gender']
# gender = input("Gender (m or f): ")
church = args['church']
# church = input("Is the funeral at the church? (y/n): ")
full_name = name
first_name = name.split()[0].capitalize()

if gender[0] in "Mm":
    gender = "masculine"
else:
    gender = "feminine"

if gender == "masculine":
	his = "his"
	he = "he"
	him = "him"
else:
	his = "her"
	he = "she"
	him = "her"

name_sliced = name.split()
slug = ("_".join(name_sliced))

def set_date(number):
    new_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    new_date = new_date + datetime.timedelta(days=number)
    return new_date

today = today.strftime('%Y-%m-%d')
# add to funeral project
project_id=project_id = '162548698'

# Now Add tasks to Todoist

api = todoist.TodoistAPI(config.todoist_api)

# # sets the notify church about death
notify_date = today
item = api.items.add('email congregation about ' + name + ' death and funeral arrangements', project_id=project_id, date_string=notify_date)

# # meet with family
item = api.items.add('Set up meeting with ' + name + ' family', project_id=project_id, date_string=notify_date)

# # mark deceased in database
item = api.items.add('mark ' + name + ' deceased in database', project_id=project_id, date_string=notify_date)

# # print backup copy of funeral
print_backup = set_date(-1)
item = api.items.add('print backup copy of funeral sermon for ' + name + ' funeral', project_id=project_id, date_string=print_backup.strftime('%Y-%m-%d'))

if church in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']:
    # check and add to church calendar
    item = api.items.add('check calendar and add funeral for ' + name + ' to calendar', project_id=project_id, date_string=notify_date)
#     # line up sound tech
    item = api.items.add('line up sound tech for ' + name + ' funeral', project_id=project_id, date_string=notify_date)

api.commit()

# Function to Grab lines of text from various subfiles and do replacements


def grab_section(file):
	with open(home + "/Dropbox/Templates/Funeral/" + file) as f:
	    lines = f.read()
	    lines = lines.replace("{full_name}", full_name)
	    lines = lines.replace("{first_name}", first_name)
	    lines = lines.replace("{he}", he)
	    lines = lines.replace("{his}", his)
	    lines = lines.replace("{him}", him)
	    lines = lines.replace("{His}", his.capitalize())
	    lines = lines.replace("{He}", he.capitalize())
	    target.write(lines)

filename =(home + '/Dropbox/Funeral_Work/' + date + "_" + slug + '.md')

if os.path.isfile(filename):
	print("File already exists")
else:
	target = open (filename, 'w')
	target.write("% {} Funeral\n".format(name))
	target.write("% Wade Allen\n")
	target.write("% {}\n\n".format(date))
	grab_section("welcome.md")
	grab_section("songs.md")
	grab_section("bio.md")
	grab_section("faith.md")
	grab_section("graveside.md")
	target.close()

