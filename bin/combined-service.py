#!/usr/bin/env python3

import todoist
import datetime
import config
import argparse
from os.path import expanduser
import os
import os.path

home = expanduser("~")

parser = argparse.ArgumentParser(description='combined service Todos')
parser.add_argument('-d','--date', default="today", help='Date of Baptism')
args = vars(parser.parse_args())

date = args['date']
today = datetime.date.today()

def set_date(number):
    new_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    new_date = new_date + datetime.timedelta(days=number)
    return new_date

def current_month(code):
    new_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    format = "%" + code
    return new_date.strftime(format)

def previous_month(code):
    new_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    first = new_date.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)
    format = "%" + code
    return lastMonth.strftime(format)

current_word = current_month("B")

previous_month_number = previous_month("m")
previous_month_year = previous_month("Y")


visitor_reminder = "{}-{}-10".format(previous_month_year, previous_month_number)
visitor_reminder = datetime.datetime.strptime(visitor_reminder, '%Y-%m-%d')

project_id=project_id = '2195611377'

api = todoist.TodoistAPI(config.todoist_api)

# Announce combined service
announce_date = set_date(-7)
item = api.items.add('Announce combined service for ' + date, project_id=project_id, date_string=announce_date.strftime('%Y-%m-%d'))

# Add to calendar
item = api.items.add('Change calendar to Reflect combined service on ' + date, project_id=project_id, date_string=today.strftime('%Y-%m-%d'))

# Make sure combined service in bulletin
bulletin_date = set_date(-13)
item = api.items.add('Make sure that combined service on ' + date + ' is in the bulletin', project_id=project_id, date_string=bulletin_date.strftime('%Y-%m-%d'))

# Make sure combined service in visitor
item = api.items.add('Make sure that combined service on ' + date + ' is in the ' + current_word + ' Visitor', project_id=project_id, date_string=visitor_reminder.strftime('%Y-%m-%d'))

# Send out congregational email for combined service
email_date = set_date(-4)
item = api.items.add('Email congregation about combined service on Sunday', project_id=project_id, date_string=email_date.strftime('%Y-%m-%d'))

# Change website for combined service
website_change_website = set_date(-7)
item = api.items.add('Change website for combined service next week in config.yaml file', project_id=project_id, date_string=website_change_website.strftime('%Y-%m-%d'))

# Change website back after combined service
change_site_back = set_date(0)
item = api.items.add('Change website back to regular schedule in config.yaml file', project_id=project_id, date_string=change_site_back.strftime('%Y-%m-%d'))

api.commit()

