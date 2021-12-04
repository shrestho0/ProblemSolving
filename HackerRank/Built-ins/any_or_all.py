

#@ LEARNING PART
## any(collection)
# print(any([ 1>0, 1==0, 1<0 ]))
# print(any([ 1<0, 2<1, 3<2 ]))

# ## all(collection)
# print(all(['a' < 'b', 'b' < 'c']))
# print(all(['a' < 'b', 'c' < 'b']))




#@ TASK
# n, arr = input(), tuple(int(x)>0 for x in input().split())
# print( all((n==n[::-1] , all(arr))) )



# # n, arr = input().strip(), tuple(int(x)>0 for x in input().strip().split())
# n, arr = all([x>0 for x in range(1, int(input()))]), any([x==x[::-2] for x in input().strip().split()])
# print(n, arr)
# # n = any == n[::-1]

# # print(n, all(arr))







# n, arr = input(), tuple(x for x in input().strip().split())

# all_pos = all([int(x) > 0 for x in arr])
# any_pal = any(x==x[::-1] for x in arr)

# print(all_pos, any_pal, arr)



n, arr = input(), tuple(x for x in input().strip().split())
print( all([ all([int(x) > 0 for x in arr]), any(x==x[::-1] for x in arr)  ]) )
