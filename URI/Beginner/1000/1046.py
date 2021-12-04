# Accepted in first attempt, Alhamdulillah 
get_timess = input().split()
start_time, end_time = (int(x) for x in get_timess)
# 24 Hour Style
if start_time > end_time:
    print(f"O JOGO DUROU {24-start_time+end_time} HORA(S)")
elif start_time < end_time:
    print(f"O JOGO DUROU {end_time-start_time} HORA(S)")
elif start_time == end_time:
    print("O JOGO DUROU 24 HORA(S)")
    