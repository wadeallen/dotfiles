from datetime import date
from dateutil.relativedelta import relativedelta, SU
format = "%Y-%m-%d"
today = date.today()
sunday = today + relativedelta(weekday=SU(-1))
date = sunday.strftime(format)
keyboard.send_keys(date)