from datetime import datetime
date_string = "19 November, 2022"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print('date_object =', date_object)