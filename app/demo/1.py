# function to calculate the date difference between two dates
def date_diff(date1, date2):
    from datetime import datetime
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((date2 - date1).days)

print(date_diff("2020-01-01", "2020-01-10"))