# -*- coding: utf-8 -*-


from albert import *
import os
from time import sleep


__title__ = "Enduring Word Commentary"
__version__ = "0.4.2"
__triggers__ = "ew "
__authors__ = "Wade Allen"
#__exec_deps__ = ["whatever"]


iconPath = os.path.dirname(__file__)+"/bible.svg"

def handleQuery(query):
    if not query.isTriggered:
        return

    term = query.string.replace(" ", "+")

    if query.isTriggered:
        return Item(id=__title__,
                    icon=iconPath,
                    text="Search Bible: " + query.string,
                    subtext="Opens Enduring Word Commentary to Passage",
                    actions=[
                        ProcAction(text='Opens Enduring Word Commentary',
                                   commandline=['open_ew', term])      
                    ])



