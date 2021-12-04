#@ Learning Part

# print(*zip([1,2,3,4,5,6], 'Hacker'))
# print(*zip([1,2,3,4,5,6], [0,9,8,7,6,5,4,3,2,1]))

# A = [1,2,3]
# B = [6,5,4]
# C = [7,8,9]

# X = [A] + [B] + [C]
# print(*zip(*X))


#@ TASK
m, n = map(int, input().split())
scores = []
for _ in range(n):
    scores.append(list(map(float, input().split())))
for _ in zip(*scores):
    print(sum(_)/n)