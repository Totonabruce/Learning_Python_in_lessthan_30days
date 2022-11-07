from datetime import datetime
new_year = datetime (2023, 1,1)
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) #1 1 2023 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2023, 0:0
