from datetime import date
from dateutil.relativedelta import relativedelta
today = date.today()
next_month = today + relativedelta(months=1) 
date = next_month.strftime("%B")
print("Dear Church Family, \n")
print("We will printing the " + date + " Visitor on the last week of this month.\n")
print("If you have an article for the Visitor, please email it to me by ")
print("type deadline here")
print("Thanks so much and have a great week.\nWade")
