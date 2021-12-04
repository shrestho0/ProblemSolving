




n, m = map(int, input().split())
reactor_count = {}

for _ in range(2): 
    x,y = input().split()
    if x not in reactor_count: 
        reactor_count[x] = 1
    else:
        reactor_count[x] += 1
    
    if y not in reactor_count: 
        reactor_count[y] = 1
    else:
        reactor_count[y] += 1
reactor_count = len([x for x in reactor_count.keys() if reactor_count.get(x) > 1])
    
print(n-reactor_count)