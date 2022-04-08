

n = input()

num = map(int, input().split())

pos = len([x for x in num if x > 0])
neg = len([x for x in num if x < 0])
zero = len([x for x in num if x == 0])

print(num)
print(pos,neg, zero)

# 6
# -4 3 -9 0 4 1
