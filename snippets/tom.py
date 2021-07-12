from datetime import date
import dateutil.relativedelta
format = "%B %Y"
today = date.today()
last_month = today + dateutil.relativedelta.relativedelta(months=-1)
date = last_month.strftime(format)
print(f"Hi Tom,\n\nHere is the reimbursement report for {date}. Please let me know if you have any questions. I hope you have a great week.\n\nBlessings,\n\nWade", end='') 
