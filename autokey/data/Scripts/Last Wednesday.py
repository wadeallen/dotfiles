from datetime import date
from dateutil.relativedelta import relativedelta, WE
format = "%Y-%m-%d"
today = date.today()
sunday = today + relativedelta(weekday=WE(-1))
date = sunday.strftime(format)
keyboard.send_keys(date)