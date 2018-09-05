#!/usr/bin/env python3

import datetime

date = '2018-09-05'

def set_date (name_var, time_var):
    name_var = datetime.datetime.strptime(date, '%Y-%m-%d') 
    name_var = name_var + datetime.timedelta(days=time_var)

set_date(test_variable, -10)

print(test_variable)
