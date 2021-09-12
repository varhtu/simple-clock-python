import datetime
import time

#reference: https://www.w3schools.com/python/python_datetime.asp

#today = datetime.date.today()
#print("Today's date:", today)

#time = datetime.time.now()
#print("Current time:", time)

while True:
    today = datetime.datetime.now()
    print(today.strftime("%A %x %X"))
    time.sleep(1)
