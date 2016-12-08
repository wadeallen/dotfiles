#!/usr/local/bin/python3

import subprocess
import sys
import json
import argparse

parser = argparse.ArgumentParser(description='Add calendar entry to Google Calendar')
parser.add_argument('-q','--quickadd', nargs='*', help='Quick Add Text',  required=True)
args = vars(parser.parse_args())

quickadd = ' '.join(args['quickadd'])

subprocess.call("gcalcli quick --calendar=wadesallen@gmail.com '" + quickadd + "'", shell=True)

print ("Calendar Event Added")
