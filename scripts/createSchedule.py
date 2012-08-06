# Creates Document with course meeting dates in Markdown format

import time
from datetime import timedelta
from datetime import date
f = open('syllabus_schedule.txt', 'w')

theDay = date(2012, 8, 28)
week = 1
heading = "### Week " + str(week) + '\n\n'
while theDay < date(2012, 12, 12):
    f.write(heading) 
    now = '#### ' + theDay.strftime("%A %B %d") + '\n\n\n'
    f.write(now)
    if theDay.weekday() == 3:
        increment = timedelta(days = 5)
        week = week + 1 			                
        heading = "### Week " + str(week) + '\n\n'
    else:        
        increment = timedelta(days = 2)
        heading = ""
    theDay = theDay + increment
