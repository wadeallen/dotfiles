#!/bin/bash

DATE=`zenity --calendar --date-format='%A, %B %d' 2>/dev/null`
echo $DATE
