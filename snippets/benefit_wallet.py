from datetime import date
from dateutil.relativedelta import relativedelta, SU
format = "%Y-%m-%d"
today = date.today()
date = today.strftime(format)
print("Benefit Wallet Receipt " + date)
