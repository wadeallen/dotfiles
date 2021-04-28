from datetime import date
from dateutil.relativedelta import relativedelta, SU
import pyclip
format = "%Y-%m-%d"
today = date.today()
date = today.strftime(format)
pyclip.copy("this is a test test")

