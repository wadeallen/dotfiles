from datetime import date
from dateutil.relativedelta import relativedelta, TH
format = "%Y-%m-%d"
today = date.today()
sunday = today + relativedelta(weekday=TH(-1))
date = sunday.strftime(format)
keyboard.send_keys(date)