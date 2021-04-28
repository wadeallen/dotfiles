#!/usr/bin/env python3

import re

with open('/home/wadeallen/.textsnippets.txt', 'r') as f:
	data = f.read()

snips = re.split("---", data)

for snip in snips:
    # strip the blank line at the end
    s = '\n'.join(snip.split('\n')[1:-1])
    #make sure we output the newlines, but no string wrapping single quotes
    print(repr(s.strip()).strip('\''))
