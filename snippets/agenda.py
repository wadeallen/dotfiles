from datetime import date
from dateutil.relativedelta import relativedelta
today = date.today()
tomorrow = today + relativedelta(days=1)
meeting_date=tomorrow.strftime("%B %d")
print(f"I have attached the agenda for the {meeting_date} meeting. Please let me know if you need to add additional items. See you tomorrow! ")
