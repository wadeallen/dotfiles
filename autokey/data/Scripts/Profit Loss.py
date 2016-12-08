from datetime import date
format = "%Y-%m"
today = date.today()
date = today.strftime(format)
keyboard.send_keys(date + "_Profit_Loss")