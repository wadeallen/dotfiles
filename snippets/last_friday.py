from datetime import date
from dateutil.relativedelta import relativedelta, FR
format = "%Y-%m-%d"
today = date.today()
sunday = today + relativedelta(weekday=FR(-1))
date = sunday.strftime(format)
print(date, end='')
