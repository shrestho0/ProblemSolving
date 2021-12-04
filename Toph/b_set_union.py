



input()
A = {int(x) for x in input().split()}
B = {int(x) for x in input().split()}
print(*sorted(A.union(B)))
