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

__title__ = "Scripture This Week"
__version__ = "0.4.2"
__triggers__ = "cs "
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
	if not query.isTriggered:
		return

	results = []

	for i in range (1,5):
		full_path = path(i)
		files = glob.glob(full_path)
		for name in files:
			post = frontmatter.load(name)
			title = post['title']
			scripture = post['scripture']
			summary = post['summary']
			if type(post['date']) is datetime.date:
				postdate = post['date']
			else:
				postdate = parser.parse(post['date'])
			results.append(
				Item(id=__title__,
					icon= iconPath,
				    text=f"{scripture}",
				    subtext=f"date: {postdate.strftime('%B %d')}",
				    actions=[
				    ClipAction(text=f"Copy Scripture to clipboard", clipboardText=scripture),
				    ClipAction(text=f"Copy Title to clipboard", clipboardText=title),
				    ClipAction(text=f"Copy Summary to clipboard", clipboardText=summary)
				    ]
				  )
				)

	return results


