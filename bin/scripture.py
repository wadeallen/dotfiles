#!/usr/bin/env python

import urllib2
import re
import sys
import json


options = ['include-passage-references=false',
           'include-first-verse-numbers=false',
           'include-verse-numbers=false',
           'include-heading-horizontal-lines=false',
           'include-footnotes=false',
           'include-footnote-body=false',
           'include-short-copyright=false',
           'include-passage-horizontal-lines=false',
           'include-headings=false',
           'include-selahs=false',
           'indent-poetry=false'
           ]

options = '&'.join(options)

# print(options)

passage = "John 2:1-3"

passage = passage.split()
passage = '+'.join(passage)
request = urllib2.Request("https://api.esv.org/v3/passage/text/?q=" + passage + '&' + options)
request.add_header('Authorization','Token ca76f7bf26d7b82f9d765305b960d2d0f71f9f6c')

request.get_header('Accept')
response = urllib2.urlopen(request)
page = response.read()

bible = json.loads(page)
bibletext = bible['passages']
bibleref = bible['canonical']

print(bibleref)
print (u", ".join(bibletext))
