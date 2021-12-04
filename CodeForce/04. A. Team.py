


koida = 0 
for i in range(int(input())):
    if sum(map(int, input().split())) >= 2: koida += 1
print(koida)
