#!/usr/bin/env python3

import datetime
from os.path import expanduser
import os
import os.path
import argparse
import config
import shutil

home = expanduser("~")

parser = argparse.ArgumentParser(description='Move Sermon PDF to Print Folder')
parser.add_argument('-n','--name', nargs='*', help='Name of File',  required=True)
args = vars(parser.parse_args())

file = args['name']
path = home + '/Documents/Sermons/' + file

print(file)
