


'''

3 99


1 2 3
4 5 6
7 8 9
10 11 12
...
97 98 99

'''

n, k = map(int, input().split())
# n,k = 3, 99

i = 1
while i <= k:
    if i % n == 0:
        print(i)
    else:
        print(i, end=" ")
    i+=1
    
