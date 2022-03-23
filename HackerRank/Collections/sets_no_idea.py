


# A te thakle lav
# B te thakle loss


# def a_bit_of_Happyness(TO_CHECK, A, B):
#     Happyness = 0
#     Happyness += len([x for x in TO_CHECK if x in A])
#     Happyness -= len([y for y in TO_CHECK if y in B])
#     return Happyness

    


# n, m = map(int, input().split())
# TO_CHECK = set(map(int, input().split()))
# A = set(map(int, input().split()))
# B = set(map(int, input().split()))

# print(a_bit_of_Happyness(TO_CHECK, A,B))

# This is one of the worst one ever

_ = input()
TO_CHECK = input().split()
A = set(input().split())
B = set(input().split())
 
HAPPYNESS = 0
for _ in TO_CHECK:
    if _ in A: HAPPYNESS += 1
    if _ in B: HAPPYNESS -= 1

print(HAPPYNESS)
