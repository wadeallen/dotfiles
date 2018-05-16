#!/bin/bash

DATE=`zenity --calendar --date-format='%Y-%m-%d' 2>/dev/null`
printf $DATE
