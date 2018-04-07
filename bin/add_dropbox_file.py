#!/usr/bin/env python

import dropbox
import datetime
import subprocess
from os.path import expanduser
import config

dbx = dropbox.Dropbox(config.dropbox_key)

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")
path='/Journal/{}.journal.markdown'.format(today)

try:
    dbx.files_get_metadata(path)
except:
    dbx.files_upload("Date: {} \n".format(today), path)





