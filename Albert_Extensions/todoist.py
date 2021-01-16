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

    if query.string.startswith("delay"):
        sleep(2)
        return Item(id=__title__,
                    icon=os.path.dirname(__file__)+"/plugin.svg",
                    text="Delayed test item",
                    subtext="Query string: %s" % query.string)

    if query.string.startswith("throw"):
        raise ValueError('EXPLICITLY REQUESTED TEST EXCEPTION!')

    info(query.string)
    info(query.rawString)
    info(query.trigger)
    info(str(query.isTriggered))
    info(str(query.isValid))

    critical(query.string)
    warning(query.string)
    debug(query.string)
    debug(query.string)

    results = []

    item = Item()

    item.icon = iconPath
    item.text = 'Python item containing %s' % query.string
    item.subtext = 'Python description'
    item.completion = __triggers__ + 'Completion Harharhar'
    item.urgency = ItemBase.Notification  # Alert, Normal
    info(item.icon)
    info(item.text)
    info(item.subtext)
    info(item.completion)
    info(str(item.urgency))
    def function(): info(query.string)
    item.addAction(FuncAction("Print info", function))
    item.addAction(FuncAction("Print warning", lambda: warning(query.string)))
    results.append(item)

    item = Item(id=__title__,
                icon=os.path.dirname(__file__)+"/plugin.svg",
                text="This is the primary text",
                subtext="This is the subtext, some kind of description",
                completion=__triggers__ + 'Hellooohooo!',
                urgency=ItemBase.Alert,
                actions=[
                    FuncAction(text="FuncAction",
                               callable=lambda: critical(query.string)),
                    ClipAction(text="ClipAction",
                               clipboardText="blabla"),
                    UrlAction(text="UrlAction",
                              url="https://www.google.de"),
                    ProcAction(text="ProcAction",
                               commandline=["espeak", "hello"],
                               cwd="~"),
                    TermAction(text="TermAction",
                               commandline=["sleep", "5"],
                               cwd="~/git"),
                    TermAction(text="TermAction",
                               script="[ -e issue ] && cat issue | echo /etc/issue not found.",
                               behavior=TermAction.CloseBehavior.DoNotClose,
                               cwd="/etc")
                ])
    results.append(item)


    # Api v 0.2
    info(configLocation())
    info(cacheLocation())
    info(dataLocation())

    return results
