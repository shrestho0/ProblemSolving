import math
import os
import random
import re
import sys
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    def get_time(T):
        T = T.split()
        Year = int(T[3])
        month_name = T[2]
        datetime_object = datetime.datetime.strptime(month_name, "%b")
        Mon = datetime_object.month
        Day = int(T[1])
        Hour = int((T[4].split(":"))[0])
        Min = int((T[4].split(":"))[1])
        Sec = int((T[4].split(":"))[2])
        Zone = T[-1]
        Zone = (datetime.datetime.strptime(Zone, "%z"))
        Zone = Zone.tzinfo

        Time = datetime.datetime(Year, Mon, Day, Hour, Min, Sec, tzinfo=Zone)
        return Time
    t1 = get_time(t1)
    t2 = get_time(t2)
    time_diff = (t1-t2)
    time_diff = math.floor(time_diff.total_seconds())
    return str(abs(time_diff))
    


t = int(input())
total = ''
for t_itr in range(t):
    t1 = input()

    t2 = input()

    delta = time_delta(t1, t2)

    total += f"{delta}\n"
print(total)
