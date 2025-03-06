import datetime as dt

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()
if year == 2025:
    print("Wear a face mask")

print(year)
print(day_of_week) # output is one. Second day of the week in this case, index counting

date_of_birth = dt.datetime(year=1998, month=9, day=12)
print(date_of_birth)