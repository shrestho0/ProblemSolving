

import math
def hour_glass(arr):
    lenx = len(arr)
    sumx = -math.inf
    for i in range(lenx-2):
        for j in range(lenx-2):
            curr_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]+ arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if curr_sum > sumx:
                sumx = curr_sum
    return sumx


arr = []
for _ in range(6):
    arr.append(tuple(map(int, input().split())))
print(hour_glass(arr))


# for i in range(lenx-2):
#     for j in range(lenx-2):
#         curr_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]+ arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
#         if curr_sum > sumx:
#             sumx = curr_sum
# print(sumx)

# 1 1 1 0 0 0           [i][j] + [i][j+1] + [i][j+2]
# 0 1 0 0 0 0           [i+1][j] + [i+1][j+1] + [i+1][j+2]
# 1 1 1 0 0 0           [i+2][j] + [i+2][j+1] + [i+2][j+2]
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0


