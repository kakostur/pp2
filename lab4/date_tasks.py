#1
from datetime import datetime, timedelta

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print(five_days_ago)


#2
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print( yesterday.strftime("%Y-%m-%d"))
print( today.strftime("%Y-%m-%d"))
print( tomorrow.strftime("%Y-%m-%d"))


#3
from datetime import datetime

current_datetime = datetime.now()
current_datetime_without_microseconds = current_datetime.replace(microsecond=0)
print(current_datetime_without_microseconds)



#4
from datetime import datetime

date1 = datetime(2023, 5, 20, 10, 30, 0)
date2 = datetime(2023, 5, 25, 15, 45, 0)

difference_seconds = (date2 - date1).total_seconds()
print(difference_seconds)
