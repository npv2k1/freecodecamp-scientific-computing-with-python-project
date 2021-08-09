from arepl_dump import dump

start = "11:06 PM"
duration = "2:02"
time, timeType = start.split()
h, m = time.split(":")
if(h=='12'): h=0
if timeType=="PM":
    sTime = int(h)*60+int(m)+60*12
else:
    sTime = int(h)*60+int(m)




dh, dm = duration.split(':')
dt = int(dh)*60+int(dm)


day = dt//(60*24)

timeCl = sTime + dt-day*24*60

new_day = day + timeCl//(60*24)
timeCl = timeCl - (timeCl//(60*24))*24*60

if((timeCl//(12*60))%2!=0):
    new_type="PM"
    new_hour = (timeCl-12*60)//60
    new_minute = (timeCl-12*60)%60
else:
    new_type="AM"
    new_hour = (timeCl)//60
    new_minute = (timeCl)%60
if(new_day>0):
    new_time = f'{new_hour}:{new_minute} {timeType}, ({new_day} days later)'
else:
    new_time = f'{new_hour}:{new_minute} {timeType}'
print(new_time)
