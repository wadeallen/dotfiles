#!/bin/bash

date=`date +"%Y-%m-%d"`

cd /home/wadeallen/Documents/Sites/fbcmuncie_2018/_posts

sed "/date: ${date}/r /home/wadeallen/Documents/Textbits/duration.txt" 2018-10-29-test.md > test.md

