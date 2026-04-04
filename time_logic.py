import time 

# when the user enter the time they want to spend doing task 

#import user_want_spend_time later will created in the main menu thingy  ()

#instead of askign add the visuaer thingy so the user jjust enter their time in 
user_want_spendtime  = input("Enter the time you want to spend doing your task in format hh:mm:ss (ex: 01:30:00): ")
hours, minutes, seconds = map(int, user_want_spendtime.split(':'))
total_seconds = hours * 3600 + minutes * 60 + seconds

for x in range(total_seconds, 0, -1):
    seconds = x % 60
    minutes = int(x/60)%60
    hours = int (x/3600)
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    time.sleep(1)

#Add the device tracker ( to track phone, laptop, etc if viewd throguht camper) )
print("Congratulations! You have completed your task in " + str(user_want_spendtime)) #Add this part if the user slack off > 0 then say "How ever u slack off x time"
