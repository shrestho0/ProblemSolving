from itertools import combinations
def char_idx(iterable, item):
    for i in iterable:
        if item == i:
            return i
n = input()
n = input().split()
k = int(input())


# print(n, k)
x = [x+1 for x in range(len(n))]
all_indices = combinations(x, k)
needed = 0
dup_index = [i+1 for i in range(len(n)) if n.count(n[i]) > 1]

for tup in all_indices:
    if len(set(tup).intersection(set(dup_index))):
        needed+=1

print('{:4f}'.format(len(n) / needed))
    
