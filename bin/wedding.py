#!/usr/local/bin/python3

import sys
import json
import todoist

import dateutil.parser
from datetime import timedelta, datetime

api = todoist.TodoistAPI('1ddba66a17f8f974360b5d479b8bd9b98d49b1ca')

date = input('Date of Wedding (include year): ')
today = datetime.now().strftime('%Y-%m-%d')
wedding_date = dateutil.parser.parse(date).strftime('%Y-%m-%d')
bride_name = input('First Name of Bride: ')

def numberDays(number):
	w_date = dateutil.parser.parse(wedding_date)
	new_date = w_date + timedelta(days=number)
	formated_date = new_date.strftime('%Y-%m-%d')
	return formated_date

def fromToday(number):
	new_date = datetime.now() + timedelta(days=number)
	formated_date = new_date.strftime('%Y-%m-%d')
	return formated_date

project = api.projects.add('{} ({})'.format(wedding_date, bride_name),indent=2, color=2)
project_id = project['id']

# Contact Sound Tech
item = api.items.add('Contact Adam or Ward about {} ({}) wedding'.format(wedding_date, bride_name), project_id, date_string=numberDays(-90))
# Follow up with Sound Tech
item = api.items.add('Follow up with Adam or Ward about {} ({}) wedding'.format(wedding_date, bride_name), project_id, date_string=numberDays(-85))
# Ask if organist/pianoist needed
piano = input('Will they be using an Organist/Pianist? [y/n]: ').lower()
if piano == 'y' or piano == 'yes':
	item = api.items.add('Email Organist Pianist Info to {} about {} wedding'.format(bride_name, wedding_date), project_id, date_string=today)
	item = api.items.add('Contact Organist Pianist about {} wedding'.format(wedding_date), project_id, date_string=today)
	item = api.items.add('Follow up with Organist Pianist about {} wedding'.format(wedding_date), project_id, date_string=fromToday(7))
else:
	print ('------\nNo organist/pianist needed\n------')
# set up meeting with Bride
item = api.items.add('Set up meeting with {} about {} wedding'.format(bride_name, wedding_date), project_id, date_string=numberDays(-90))
# send email about arrival times
item = api.items.add('Send email to {} about arrival times'.format(bride_name), project_id, date_string=numberDays(-14))
# unlock doors
item = api.items.add('Set doors for {} wedding'.format(wedding_date), project_id, date_string=numberDays(-7))
# final payments
item = api.items.add('Remind {} about final payments'.format(bride_name), project_id, date_string=numberDays(-7))
# damage deposit return
item = api.items.add('Request damage deposit refund for {}'.format(bride_name), project_id, date_string=wedding_date)

api.commit()

print ('------\n{} Wedding Added to Todoist\n------'.format(wedding_date))



