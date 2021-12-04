


# n, vag_hobe = [int(x) for x in input().split()]
# S = 0
# # for _ in range(n): 
# #     S = max(map(int, input().split()[1:]))**2
# for _ in range(n):
#     S =
#     # (a * M + b)^2 % M

# print(S%vag_hobe)


from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))