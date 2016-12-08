from datetime import date
format = "%Y-%m-%d"
today = date.today()
date = today.strftime(format)
keyboard.send_keys(date)