from datetime import date
from dateutil.relativedelta import relativedelta, TU
format = "%Y-%m-%d"
today = date.today()
sunday = today + relativedelta(weekday=TU(-1))
date = sunday.strftime(format)
print(date)
