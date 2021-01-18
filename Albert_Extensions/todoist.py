# -*- coding: utf-8 -*-


from albert import *
import os
from time import sleep


__title__ = "Todoist"
__version__ = "0.4.2"
__triggers__ = "t "
__authors__ = "Wade Allen"
#__exec_deps__ = ["whatever"]


iconPath = os.path.dirname(__file__)+"/todoist.svg"



def handleQuery(query):
    if not query.isTriggered:
        return

    if query.isTriggered:
        return Item(id=__title__,
                    icon=iconPath,
                    text="Add Task: " + query.string,
                    subtext="Type Task (Don't forget to include date)",
                    actions=[
                    	FuncAction("Add Todo", lambda: os.system(f"(/home/wadeallen/bin/todoist '{query.string}')&"))
                    ])



