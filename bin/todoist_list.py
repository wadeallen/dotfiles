#!/usr/local/bin/python3

import todoist
import sys
import config

api = todoist.TodoistAPI(config.todoist_api)

def list_tasks(query):
    today = api.query([query])
    print ('<?xml version="1.0"?> <items>')
    if today[0]['data']:
    	for item in today[0]['data']:
    		print ('<item uid="desktop" arg="' + (str(item['id'])) + '" valid="YES" autocomplete="Desktop" type="file">', \
                '<title>' + (item['content']) + '</title>', \
                '<subtitle>Complete Task</subtitle>', \
                '<icon>/Users/wadeallen/Pictures/todoist.png</icon>', \
            	'</item>')
    else:
    	print (
    		"""
    		<item uid="none" arg="none">
            <title>Nothing to Do</title>
            <subtitle>Everything is Complete</subtitle>
            <icon></icon>
        	</item>
        	"""
        	)
    print ('</items>')

def add_task_list(task,date):
    print ('<?xml version="1.0"?> <items>')
    print ('<item uid="desktop" arg="' + task + '" valid="YES" autocomplete="Desktop" type="file">', \
                '<title>Add Task: ' + task + ' on ' + date + '</title>', \
                '<subtitle>Complete Task</subtitle>', \
                '<icon>/Users/wadeallen/Pictures/todoist.png</icon>', \
                '</item>')
    print ('</items>')

if sys.argv[1] == 'tod':
    list_tasks('overdue, today')
elif sys.argv[1] == 'tom':
    list_tasks('tomorrow')
    

