import datetime as dt

now = dt.datetime.now()
print(f"now: {now}")

year = now.year
print(f"now.year: {year}")

if year == 2026:
    print("The year is 2026")

day_of_week = now.weekday()
print(f"day_of_week: {day_of_week} (0 = Monday, 1 = Tuesday, ...)")

date_of_birth = dt.datetime(year=2005, month=4, day=9, hour=20, minute=14)
print(date_of_birth)