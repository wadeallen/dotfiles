#!/usr/bin/env python3

from albert import *
import os
import glob
from datetime import date 
from os.path import expanduser
import datetime
from dateutil import parser

__title__ = "Snippets"
__version__ = "0.4.2"
__triggers__ = "sn "
__authors__ = "Wade Allen"

iconPath = os.path.dirname(__file__)+"/copy.svg"

home = expanduser("~")

def handleQuery(query):
	if not query.isTriggered:
		return

	if query.isTriggered:
		query.disableSort()

	stripped = query.string.strip()

	results = []

	for file in glob.glob(f"/home/wadeallen/dotfiles/snippets/*{stripped}*.py"):
		base = os.path.basename(file)
		short_name = os.path.splitext(base)[0]
		results.append(
				Item(id=__title__,
					icon= iconPath,
				    text=f"{short_name}",
				    subtext=f"Copy {short_name} to Clipboard",
				    actions=[
				      ProcAction(text='Runs python script',
                                   commandline=['copy_snippet', file])
				    ]
				  )
				)

	return results


