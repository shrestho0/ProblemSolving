




n = 22
result = []
while True:
    result.append(n)
    if n==1: break
    if n % 2 == 1:
        n = 3*n +1
    else:
        n //= 2
    

print(result.__len__())