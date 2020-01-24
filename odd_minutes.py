from datetime import datetime

minutes = []

for i in range(1, 60, 2):
    minutes.append(i)

print(minutes)

right_this_minute = datetime.today().minute

if right_this_minute in minutes:
    print("This is an odd minute.")

else:
    print("Not an odd minute")

    
    


