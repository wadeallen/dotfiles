#!/usr/bin/env python3

import datetime
from os.path import expanduser
import os
import os.path
import todoist
import config
from titlecase import titlecase
from datetime import datetime, timedelta
import calendar

# Now Add tasks to Todoist

api = todoist.TodoistAPI(config.todoist_api)

month=int(input("Month (number with no leading zeros): "))
# year=int(input("Year: "))

year=2021

first_day_of_month = datetime(year, month, 1)
first_monday = first_day_of_month + timedelta(days=((0-calendar.monthrange(year,month)[0])+7)%7)
# 0 is monday of week
second_monday = first_monday + timedelta(days=7)
third_monday = first_monday + timedelta(days=14)

def set_date(number):
    new_date = third_monday + timedelta(days=number)
    new_date = new_date.strftime('%Y-%m-%d')
    return new_date

#function to add item
def addTodo(days,task,assigned=None):
	if days == 0:
		notify_date = third_monday.strftime('%Y-%m-%d')
	else:
		notify_date = set_date(days)
	item = api.items.add(f"OB: {task}", project_id=2262138501, date_string=notify_date,responsible_uid=assigned)

wade_uid = 1164489
carolyn_uid = 32108993

addTodo(-7, "email reminder and call for reports/agenda items", wade_uid)
addTodo(-4, "compile reports", carolyn_uid)
addTodo(-4, "send agenda items to Wade", carolyn_uid)
addTodo(-4, "send agenda to Karen for input", wade_uid)
addTodo(-3, "email reports for meeting/ask for additional agenda items", carolyn_uid)
addTodo(0, "email agenda/Zoom Link reminder", wade_uid)
addTodo(1, "email summmary/action items", wade_uid)
addTodo(1, "archive agenda and reports (run create_ob_meeting)", wade_uid)


api.commit()

# data=api.projects.get_data(2262138501)
# print(data)