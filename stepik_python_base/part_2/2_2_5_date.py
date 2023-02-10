import datetime

g, m, d = map(int, input().split())
delta = datetime.timedelta(days=int(input()))
data = datetime.date(g, m, d)
new_data = data + delta
print(new_data.year, new_data.month, new_data.day)
