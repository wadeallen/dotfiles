#!/usr/local/bin/python3

import sys
import json
import todoist
import config

api = todoist.TodoistAPI(config.todoist_api)
# task_id = sys.argv[1]

today = api.query(["today"])

if today[0]['data']:
    for item in today[0]['data']:
        # print ('- ' + (item['content']))
                print ('- ' + (item['content']))

# item = api.items.get_by_id(task_id)
# item.close()
# api.commit()
# print (item['content'])


