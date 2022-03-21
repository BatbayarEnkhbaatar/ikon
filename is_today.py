from datetime import datetime, date, time
import pytz
tz = pytz.timezone("Asia/Ulaanbaatar")
def is_today(p_date):
    the_date = date.today()
    day_today = datetime.combine(the_date, time())
    p_date = datetime.strptime(p_date, '%Y-%m-%d %H:%M')
    print(p_date)
    if p_date > day_today:
        return [True, p_date]
    else:
        return [False, p_date]
input = "2022-03-20 01:49"
print(is_today(input))