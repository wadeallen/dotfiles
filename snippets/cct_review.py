from datetime import date
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
import subprocess
today = date.today()
next_month = today + relativedelta(months=1) 
date = next_month.strftime("%B")
meeting = subprocess.run('/home/wadeallen/bin/choose_calendar2.sh', stdout=subprocess.PIPE)

print('The Church Coordination Team met this week. Here is a brief summary of the meeting along with budget reports. Please feel free to contact team members with questions. There are printed copies available in the church office if you know someone who does not have internet access.')
print('http://reports.fbcmuncie.org/' + meeting.stdout.decode('utf-8') + '_CCT.pdf')
print('Have a great week,')
print('Wade')
