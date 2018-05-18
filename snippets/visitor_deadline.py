from datetime import date
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
import subprocess
today = date.today()
next_month = today + relativedelta(months=1) 
date = next_month.strftime("%B")
deadline = subprocess.run('/home/wadeallen/bin/choose_calendar.sh', stdout=subprocess.PIPE)
print("We will be printing the " + date + " Visitor on the last week of this month.")
print("If you have an article for the Visitor, please email it to me by ")
print(deadline.stdout.decode('utf-8'))
print("Thanks so much and have a great week.\nWade")
