from datetime import date
from dateutil.relativedelta import relativedelta, SU
format = "%Y-%m-%d"
today = date.today()
day_of_month = int(today.strftime("%-d"))
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")
if day_of_month <= 15:
	date = f"{year}-{month}-15"
else:
	date = f"{year}-{month}-30"
print(f"{date}_Paystub", end='')

