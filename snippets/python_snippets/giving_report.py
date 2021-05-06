from datetime import date
from dateutil.relativedelta import relativedelta, SU
format = "%Y-%m-%d"
today = date.today()
sunday = today + relativedelta(weekday=SU(-2))
date = sunday.strftime(format)
print(date + " Giving Report")
