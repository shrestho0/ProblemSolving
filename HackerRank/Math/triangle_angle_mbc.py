
import math

AB, BC = int(input()), int(input())

def tri_mbc(AB=AB, BC=BC):
    return round(math.degrees(math.atan2(AB, BC)))

print(f"{tri_mbc()}{chr(176)}")