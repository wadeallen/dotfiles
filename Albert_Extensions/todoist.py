# -*- coding: utf-8 -*-

"""This is a simple python template extension.

This extension should show the API in a comprehensible way. Use the module docstring to provide a \
description of the extension. The docstring should have three paragraphs: A brief description in \
the first line, an optional elaborate description of the plugin, and finally the synopsis of the \
extension.

Synopsis: <trigger> [delay|throw] <query>"""

from albert import *
import os
from time import sleep


__title__ = "Todoist"
__version__ = "0.4.2"
__triggers__ = "todo "
__authors__ = "Wade Allen"
#__exec_deps__ = ["whatever"]


iconPath = os.path.dirname(__file__)+"/todoist.svg"



def handleQuery(query):
    if not query.isTriggered:
        return

    # Note that when storing a reference to query, e.g. in a closure, you must not use
    # query.isValid. Apart from the query beeing invalid anyway it will crash the appplication.
    # The Python type holds a pointer to the C++ type used for isValid(). The C++ type will be
    # deleted when the query is finished. Therfore getting isValid will result in a SEGFAULT.

    if query.isTriggered:
        return Item(id=__title__,
                    icon=iconPath,
                    text="Add Task: " + query.string,
                    subtext="Type Task (Don't forget to include date)",
                    actions=[
                    	FuncAction("Add Todo", lambda: os.system(f"(/home/wadeallen/bin/todoist '{query.string}')&"))
                    ])



