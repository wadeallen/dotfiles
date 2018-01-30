from datetime import date
from dateutil.relativedelta import relativedelta

today = date.today()
format = "%Y-%m-%d"
expire_date = today + relativedelta(+30)

print('*' * 5 )
print("\n---\ntitle: Title\nweight: 3\nexpire: {}\npublications: ['bulletin', 'website', 'visitor']\n---\n\n".format(expire_date))
