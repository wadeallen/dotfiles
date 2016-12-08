from datetime import date
from dateutil.relativedelta import relativedelta, SA
format = "%Y-%m-%d"
today = date.today()
sunday = today + relativedelta(weekday=SA(-1))
date = sunday.strftime(format)
keyboard.send_keys(date)