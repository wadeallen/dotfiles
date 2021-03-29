from datetime import date
from dateutil.relativedelta import relativedelta, TU
today = date.today()
next_tuesday = today + relativedelta(weekday=TU(+1))
meeting_date=next_tuesday.strftime("%a, %B %d")
print(f"I have attached the agenda for the {meeting_date} meeting. Please let me know if you need to add additional items. See you tomorrow! ")
