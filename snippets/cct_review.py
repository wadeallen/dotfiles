import datetime
yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
print('The Church Coordination Team met this week. Here is a brief summary of the meeting along with budget reports. Please feel free to contact team members with questions. There are printed copies available in the church office if you know someone who does not have internet access.\n')
print('http://reports.fbcmuncie.org/' + yesterday.strftime("%Y-%m-%d") + '_CCT.pdf\n')
print('Have a great week,\n')
print('Wade')

