from datetime import date
format = "%Y-%m"
today = date.today()
date = today.strftime(format)
print(date + "_Profit_Loss")
