import time

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def parse_time(time_str):
    try:
        h, m, s = map(int, time_str.split(':'))
        return h * 3600 + m * 60 + s
    except:
        return 0

def time_counter():
    user_want_spendtime = input("Enter the time you want to spend doing your task in format hh:mm:ss (ex: 01:30:00): ")
    hours, minutes, seconds = map(int, user_want_spendtime.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds

    for x in range(total_seconds, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        time.sleep(1)

    # Add the device tracker ( to track phone, laptop, etc if viewed through camera detection ) ) * implement later
    print("Congratulations! You have completed your task in " + str(user_want_spendtime))  # Add this part if the user slack off > 0 then say "However you slack off x time"

def get_computer_time():
    # get computer time so when the user set up time in the sticky node , tell them like when they need this task finish when the task is finish , play the sound and print : "time up". Ex if the user choose to like wake em up at 13:20 when the
    # enter the time at 12:30. When the time is at 12:30, it will play the sound "      " then turn off the sound after 3 second
    pass

