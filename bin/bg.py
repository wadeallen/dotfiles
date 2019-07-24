#!/usr/bin/env python3

from bs4 import BeautifulSoup
from sys import argv
import requests, urllib

query = argv[1]
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

if len(argv) == 3:
    version = argv[2]
    url = f'http://www.biblegateway.com/passage/?search={urllib.parse.quote_plus(query)}&version={version}&interface=print'
else:
    url = f'http://www.biblegateway.com/passage/?search={urllib.parse.quote_plus(query)}&version=NIV'

def print_info(container):
    for child in container:
        try:
            print (child.get_text())
        except:
            pass

r = requests.get(url, headers=headers)
if r.status_code == 200:
    soup = BeautifulSoup(r.content, 'html.parser')
    container = soup.find('div', {'class': 'result-text-style-normal'})
    if container:
        print_info(container)
    else:
        print (f'I do not recognize "{query}", please try again')
else:
    print ('There was an error processing, please try again')
