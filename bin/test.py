#!/usr/bin/env python3

import datetime

date = '2018-09-05'

def set_date(number):
    new_date = datetime.datetime.strptime(date, '%Y-%m-%d') 
    new_date = new_date + datetime.timedelta(days=number)
    return new_date

test = set_date(1)
print(test)
