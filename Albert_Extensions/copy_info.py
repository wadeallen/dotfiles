#!/usr/bin/env python3

from albert import *
import frontmatter
import os
import glob
from datetime import date 
from dateutil.relativedelta import relativedelta, SU
from os.path import expanduser
import datetime
from dateutil import parser

__title__ = "Copy Sermon Info for Twist"
__version__ = "0.4.2"
__triggers__ = "ci "
__authors__ = "Wade Allen"

iconPath = os.path.dirname(__file__)+"/bible.svg"

home = expanduser("~")

sermon_path = f"{home}/Dropbox/Sermon_Work"

today = date.today() 
format = '%Y-%m-%d'

def path(week):
	t_date = today + relativedelta(weekday=SU(+week))
	t_date_formatted = t_date.strftime(format)
	path = f"{sermon_path}/{t_date_formatted}_sermon.md"
	return path

def handleQuery(query):
    if query.isTriggered:
        if not query.isValid:
            return

        if query.string.strip():
            return findsermons(query)

def findsermons(query):
	for i in range(1,9):
		return [
            Item(
                id="test",
                icon=iconPath,
                text="Is internet working?",
                subtext="We could not query, check your internet connection",
                completion=query.rawString,
            	)
        	]



