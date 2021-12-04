# Done, Alhamdulillah after a big shot
get_timess = input().split()
start_hour, start_min, end_hour, end_min = (int(x) for x in get_timess)
total_time, total_hour, total_min = 0, 0, 0
# 24 Hour Style
# Make all all times in min
# Then, print hours and mins seperately

start_time = start_hour * 60 + start_min
end_time = end_hour * 60 + end_min
time_diff = end_time - start_time

if time_diff <= 0:
    time_diff+= 1440

total_time = time_diff


total_hour = total_time // 60
total_min = total_time % 60

# 1440

if total_time >= 1 and total_time <= 1440:
    print(f"O JOGO DUROU {total_hour} HORA(S) E {total_min} MINUTO(S)")