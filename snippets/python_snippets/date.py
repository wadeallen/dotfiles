from datetime import date
import pyclip

format = "%Y-%m-%d"
today = date.today()
date = today.strftime(format)
pyclip.copy(date)
