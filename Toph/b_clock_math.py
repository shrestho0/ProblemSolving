

def clock_angle(h, m):
    if h < 0 or m < 0 or h > 12 or m > 60: pass
    if h == 12: h = 0
    if m == 60:
        m, h = 0, h+1
        if h > 12:
            h = h-12

    hour_x = 0.5 * (h * 60 + m)
    mint_x = 6 * m
    angle = abs(hour_x - mint_x)
    angle = min(360-angle, angle)

    return angle


print(f"{clock_angle(*map(int, input().split())):.7f}")























# Hour, Min = map(int, input().split())

# angle = 360 - (30*Hour - 5.5*Min)

# print()


# Hour, Min = map(int, input().split())
# angle = 360 - (30*Hour - 5.5*Min)
# if angle >= 360:
#     angle -= 360

# print(f'{angle:.7f}')



# 10 15 142.5000000
# 12 30 165.0000000
