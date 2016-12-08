from datetime import date
from dateutil.relativedelta import relativedelta
today = date.today()
next_month = today + relativedelta(months=1) 
date = next_month.strftime("%B")
date_number = next_month.strftime("%Y-%m")
keyboard.send_keys("Dear Church Family, \n")
keyboard.send_keys("I wanted to let you know that the " + date + " Visitor is now available online. You can find it at the link below\n")
keyboard.send_keys("http://visitor.fbcmuncie.org/visitor_" + date_number + ".pdf\n")
keyboard.send_keys("A few of you have mentioned that the text on the newsletter is extremely small. You should be able to fix this by clicking on the View Menu and choose Zoom In. You might have to do this several times for your desired size.\n")
keyboard.send_keys("Have a great week.\nWade")
