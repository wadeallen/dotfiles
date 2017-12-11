from datetime import date
from dateutil.relativedelta import relativedelta, FR
format = "%Y-%m-"
today = date.today()
sunday = today + relativedelta(months=1)
date = sunday.strftime(format)
print(date)
