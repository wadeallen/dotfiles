from datetime import date
from dateutil.relativedelta import relativedelta, TU
today = date.today()
next_tuesday = today + relativedelta(weekday=TU(+1))
date = next_tuesday.strftime("%B %d")
print("This is a reminder to submit this report by noon on Monday. This will help me form the agenda for Tuesday's meeting. Again, you do not have to answer every question. These questions will serve as a prompt to get you thinking about what can be shared ahead of time (in writing) and what needs to be addressed in the meeting.\n")
print("What has happened in your ministry area (since the last meeting) that needs to be shared?\n")
print("What is happening in the next week or two that needs to be shared?\n")
print("What ministry teams/committees met in your area over the past week?\n")
print(f"What issues or concerns need to be discussed in the {date} staff meeting?\n")
print("How can other staff members help you this week?\n")
print(f"Will you be able to attend the {date} meeting?\n")

