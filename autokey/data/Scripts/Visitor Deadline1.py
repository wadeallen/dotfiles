from datetime import date
from dateutil.relativedelta import relativedelta
today = date.today()
next_month = today + relativedelta(months=1) 
date = next_month.strftime("%B")
retCode, deadline = dialog.input_dialog("Deadline", "What is the deadline?")
keyboard.send_keys("Dear Church Family, \n")
keyboard.send_keys("We will printing the " + date + " Visitor on the last week of this month.\n")
keyboard.send_keys("If you have an article for the Visitor, please email it to me by ")
keyboard.send_keys(deadline + ".\n")
keyboard.send_keys("Thanks so much and have a great week.\nWade")
