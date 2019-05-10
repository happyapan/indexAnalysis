import datetime


def qi_huo_next_month():
    today = datetime.datetime.today()
    year = today.year
    month = today.month
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

    next_month = datetime.datetime(year, month, 1)
    return next_month.strftime('%Y%m')[2:]


def today():
    return datetime.datetime.now().strftime('%Y%m%d')


# 获得N天之后的事情，正负值都可以
def day_after(pre_day):
    now = datetime.datetime.now()
    delta = datetime.timedelta(pre_day)
    n_days = now + delta
    return n_days.strftime('%Y%m%d')


def pre_year_date():
    today_date = datetime.datetime.today()
    return datetime.datetime(today_date.year - 1, today_date.month, today_date.day).strftime('%Y%m%d')