#!/usr/bin/env python3

#coding: utf-8
#!/usr/bin/env python
# Sample code by Christian Wyglendowski found at http://www.esvapi.org/api#verse
# Adapted for Editorial by @pfcbenjamin
# Please read the conditions of use at [ESV Bible Web Service Introduction](http://www.esvapi.org/)
# This script makes use of the non-commercial access component.From the ESV's site: "You can access the ESV text using the key "IP" (without the quotes). This key limits you to 5,000 queries per day from a single IP address. You are bound by the below conditions of use, including the non-commercial aspects"
# Please ensure you are using this within the terms granted by the Crossway.

import urllib
import sys
import re

class ESVSession:
    def __init__(self, key):
        options = ['include-short-copyright=0',
                   'output-format=plain-text',
                   'include-passage-horizontal-lines=0',
                   'include-heading-horizontal-lines=0',
                   'include-headings=0',
                   'include-subheadings=0',
                   'include-selahs=0',
                   'line-length=0',
                   'include-passage-references=0',
                   'include-footnotes=0']
        self.options = '&'.join(options)
        self.baseUrl = 'http://www.esvapi.org/v2/rest/passageQuery?key=IP'

    def doPassageQuery(self, passage):
        passage = passage.split()
        passage = '+'.join(passage)
        url = self.baseUrl + '&passage=%s&%s' % (passage, self.options)
        page = urllib.urlopen(url)
        return page.read()

    def PassageLink(self, passage):
    		clean = re.sub('\s','%20',passage)
    		link = 'http://www.esvbible.org/' + clean
    		return link

try:
    key = sys.argv[1]
except IndexError:
    key = 'IP'

bible = ESVSession(key)

p = workflow.get_variable('reference')
passage = p.replace(u'\u2013','-')
bibletext = bible.doPassageQuery(passage)
passagelink = bible.PassageLink(passage)

workflow.set_variable('bible text', bibletext)
workflow.set_variable('passagelink', passagelink)
