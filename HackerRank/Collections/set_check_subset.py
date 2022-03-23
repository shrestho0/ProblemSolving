
 
a = []
b = []
for _ in range(int(input())):
    input() #testcase of A's elements
    A = {x for x in input().split()}
    a.append(A)
    input()
    B = {x for x in input().split()}
    b.append(B)

    if A.issubset(B):
        print(True)
    else:
        print(False)
# 
# print(a,b)

