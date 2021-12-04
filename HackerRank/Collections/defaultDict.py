

# from collections import defaultdict

# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")

# for i in d.items():
#     print(i)



# 5 2
# a
# a
# b
# a
# b
# a
# b
# from collections import defaultdict
# a_count, b_count = map(int, input().split())
# # a_pos, b_pos = []
# all = []
# pos = defaultdict(list)
# for i in range(a_count+b_count):
#     x = input()



# print(a_count, b_count)
# print(pos)


from collections import defaultdict
d = defaultdict(list)

n, m = map(int, input().split())

for i in range(1,n+1):
    d[input()].append(str(i))
    
for i in range(m):
    print(' '.join(d[input()]) or -1)