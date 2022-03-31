












import math
def ascii_progress_bar(per: float):
    return '[' + '+'*math.floor(per/10) + '.'*(10-math.floor(per/10)) + '] ' + str(math.floor(per)) + '%'

print(ascii_progress_bar(float(input())))




