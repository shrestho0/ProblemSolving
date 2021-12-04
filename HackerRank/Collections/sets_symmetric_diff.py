

#@ Sets
## Learning

# a = input()
# lis = a.split()
# print(lis)

# newlis = list(map(int, lis))
# print(newlis)

# ### Creating Sets
# myset = {1,2} # Directly assigning values
# myset = set() # Initializing a set
# myset = set(['a', 'b']) # Creating a new set
# print(myset)

# ### Modifying Sets
# myset.add('c')
# print(myset)
# myset.add('a')
# myset.add((5,4))
# print(myset)

# ### Updating a set
# myset.update([1,2,3,4])
# print(myset)
# myset.update({1,7,8})
# myset.update({1,6},[5,13])
# print(myset)

# ### Removing Items
# myset.discard(10)
# print(myset)
# myset.remove(13)

# print(myset)

# ### Common Set Operations
# a = {2,4,5,9}
# b = {2,4,11,12}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))

# ### Union Intersection Methods are Symmetric methods
# print(a.union(b) == b.union(a))
# print(a.intersection(b) == b.intersection(a))
# print(a.difference(b) == b.difference(a))



#@ TASK

n1 = int(input())
m1 = set(map(int, input().split()))
n2 = int(input())
m2 = set(map(int, input().split()))

def karbar(n1,m1,n2,m2):
    x = list(m1.difference(m2))
    y = list(m2.difference(m1))
    print(*sorted((x+y)), sep="\n")

karbar(n1, m1, n2, m2)