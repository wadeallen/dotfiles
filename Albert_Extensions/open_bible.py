# -*- coding: utf-8 -*-


from albert import *
import os
from time import sleep


__title__ = "Open Bible"
__version__ = "0.4.2"
__triggers__ = "bi "
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
                    subtext="Opens Biblegateway.com to Passage",
                    actions=[
                        ProcAction(text='Opens Biblegateway',
                                   commandline=['open_bible', term])      
                    ])



