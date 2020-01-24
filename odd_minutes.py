from datetime import datetime
import time
import random


minutes = []

for i in range(1, 60, 2):
    minutes.append(i)

count = 1

for i in range(5):

    right_this_minute = datetime.today().minute
    
    if right_this_minute in minutes:
        print("This is an odd minute.")
        time.sleep(random.randint(1,60))
        count+=1

    else:
        print("Not an odd minute")
        time.sleep(random.randint(1,60))
        count+=1





