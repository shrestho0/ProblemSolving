



arr = []
n,m = map(int, input().split())
for _ in range(m): arr.append([int(x) for x in input().split()])


# print(arr)
print('@===========@')
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         print(arr[i][j], end=" ")
#     print()
array = [0]*(n+1)
for _ in range(m):
    for q in arr:
        a = q[0]-1
        b = q[1]
        k = q[2]
        array[a] += k
        array[b] -= k
print(array)

