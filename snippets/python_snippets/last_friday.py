from datetime import date
from dateutil.relativedelta import relativedelta, FR
import pyclip
format = "%Y-%m-%d"
today = date.today()
sunday = today + relativedelta(weekday=FR(-1))
date = sunday.strftime(format)
pyclip.copy(date)
