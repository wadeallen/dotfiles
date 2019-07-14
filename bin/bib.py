#!/usr/bin/env python3

import xml.etree.ElementTree as ET

version = '/home/wadeallen/bibles/NIV/NIV.xml'

tree = ET.parse(version)
root = tree.getroot()

# for child in root:
# 	print(child.tag, child.attrib)

# for book in root.iter('b'):
# 	print(book.attrib)

for verse in root.findall("./b[@n='Genesis']/c[@n='3']/v[@n='4']"):
	print(verse.text)


# print books of the bible


	# if (book.attrib['n']) == "Genesis":
	# 	print(book.attrib['n'])
