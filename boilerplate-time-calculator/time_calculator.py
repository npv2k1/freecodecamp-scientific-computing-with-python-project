def add_time(start, duration, *arg):

    weeks = ["Monday", 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

    # to 24h type start day 0, 00:00
    time, time_type = start.split()
    time_hours, time_minutes = time.split(":")
    if(time_hours == '12'):
        time_hours = 0
    if time_type == "PM":
        start_time = int(time_hours)*60+int(time_minutes)+60*12
    else:
        start_time = int(time_hours)*60+int(time_minutes)

    # total minute duration
    duration_hours, duration_minutes = duration.split(':')
    duration = int(duration_hours)*60+int(duration_minutes)

    time_remaining = start_time + duration

    # day
    new_day = time_remaining//(60*24)

    time_remaining %= (24*60)

    if((time_remaining//(12*60)) % 2 != 0):
        new_type = "PM"
        new_hour = (time_remaining-12*60)//60       
        new_minute = (time_remaining-12*60) % 60
    else:
        new_type = "AM"
        new_hour = (time_remaining)//60       
        new_minute = (time_remaining) % 60
    if(new_hour == 0):
        new_hour = 12
    # Output
    if(len(arg) > 0):
        start_week = weeks.index(arg[0].capitalize())
        new_week = weeks[(start_week+1+new_day) % 7-1]
        if(new_day > 1):
            new_time = f'{new_hour}:{str(new_minute).zfill(2)} {new_type}, {new_week} ({new_day} days later)'
        elif (new_day == 1):
            new_time = f'{new_hour}:{str(new_minute).zfill(2)} {new_type}, {new_week} (next day)'
        else:
            new_time = f'{new_hour}:{str(new_minute).zfill(2)} {new_type}, {new_week}'
    else:
        if(new_day > 1):
            new_time = f'{new_hour}:{str(new_minute).zfill(2)} {new_type} ({new_day} days later)'
        elif (new_day == 1):
            new_time = f'{new_hour}:{str(new_minute).zfill(2)} {new_type} (next day)'
        else:
            new_time = f'{new_hour}:{str(new_minute).zfill(2)} {new_type}'
    return new_time
