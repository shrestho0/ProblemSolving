


## Practice Portion
# from itertools import product

# x = list(product([1,2,3,4], repeat=2))
# y = list(product([1,2,3],[3,4]))

# A = [[1,2,3], [3,4,5]]
# A = list(product(*A))

# B = [ [1,2,3], [3,4,5], [7,8]]
# B = list(product(*B))


# print(x)
# print(y)
# print(A)
# print(B)


from itertools import product
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

print(*product(A,B))
#  1 2
#  3 4
