#!/usr/bin/env python3

from urllib.request import urlopen

def internet_on():
   try:
    response = urlopen('https://www.google.com/', timeout=10)
    return True
   except: 
    return False


if internet_on():
	print("connected to internet")
else:
	print("no internet")
