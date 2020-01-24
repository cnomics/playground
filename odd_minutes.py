from datetime import datetime
import time
import random


minutes = []

for i in range(1, 60, 2):
    minutes.append(i)

right_this_minute = datetime.today().minute

print(right_this_minute)

count = 1

while count <= 5:
    if right_this_minute in minutes:
        print("This is an odd minute.")
        time.sleep(60)
        count+=1

    else:
        print("Not an odd minute")
        time.sleep(60)
        count+=1





