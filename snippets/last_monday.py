from datetime import date
from dateutil.relativedelta import relativedelta, MO
format = "%Y-%m-%d"
today = date.today()
sunday = today + relativedelta(weekday=MO(-1))
date = sunday.strftime(format)
print(date)
