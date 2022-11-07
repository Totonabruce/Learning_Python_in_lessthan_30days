from calendar import month
import datetime
from sqlite3 import Timestamp
print(dir(datetime))
['MAYEAR','MINYEAR','_built_','_cached_','_doc_','_file_','_loader_','_name_','_paackage_','_spec_','date','datetime','datetime_CAPI','sys','time','timedelta','timezone','tzinfo']

from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute =now.minute
second = now.second
Timestamp = now.timestamp()
print(day, month, year, hour, minute)
print (f'{day}/{month}/{year}, {hour}:{minute}')