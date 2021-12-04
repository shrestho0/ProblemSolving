import numpy

# 1 2 3
# 4 5 6
# 9 8 9


# 4 5 6
# 9 8 9
# arr = []

# for i in range(int(input())):
#     arr.append(tuple((int(x) for x in input().split())))

# arr = numpy.array(arr, int)
# r_diag = sum(numpy.diag(arr))
# l_diag = sum(numpy.diag(numpy.fliplr(arr)))

# print(abs(r_diag-l_diag))

# Numpy wont work. Have to do it manually.


arr = []

for i in range(int(input())):
    arr.append(tuple((int(x) for x in input().split())))
# print(arr)
print('========')
distance = 0
for i in range(len(arr)):
    distance += arr[i][i]
    distance -= arr[i][-i-1]


print(abs(distance))