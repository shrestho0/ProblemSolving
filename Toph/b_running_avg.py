
# '''
# 3
# 4 2 7
# '''

# # def running_avg(n, arr):
# #     for i in range(n):
# #         print(sum(arr[:i+1])/(i+1) )


# # running_avg(int(input()), list(map(int, input().split())))

# n = int(input())
# arr = tuple(int(x) for x in input().split())
# arr = tuple(sum(arr[:i+1])/(i+1) for i in range(n))
# print(*arr, sep="\n")





# from os import sep


# n = int(input())
# listo = tuple(map(int, input().split()))
# listo = tuple(sum(listo[:x])/x for x in range(1, n+1))


# print(*listo, sep="\n")

 

# input()
# prev = 0
# for i, value in enumerate(input().split()):
