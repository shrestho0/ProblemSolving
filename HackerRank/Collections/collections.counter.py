



# Learning Part
# from collections import Counter

# myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]

# print(Counter(myList))
# print(Counter(myList).items())
# print(Counter(myList).keys())
# print(Counter(myList).values())


# X = Number of Shoes 0<X<10^3
# N = Number of Customers 0 <N<10^3
# shoe_size = Shoe size desied by the customer
# xi = Price of the shoe


temp = 0
shoe_size_count = int(input()) # dudh bhat
shoe_size = [int(x) for x in input().split()]
ache = []
for i in range(int(input())):
    x = list(map(int, input().split()))
    if x[0] in shoe_size:
        shoe_size.remove(x[0])
        temp+= x[1]
print(temp)
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

# print(shoe_size)