




# is_prime funcition Series Short Version
# Author: Shrestho
# Author URI: https://shrestho.me

def is_prime(n: int) -> list:
    if n == 0 or n == 1: return False
    for i in range(2, n//2+1, 1):
        if n % i == 0: return False
    return True



for i in range(100): print(i, end=", ") if is_prime(i) else None

# # ANOTHER DEBUGGING TOOL
# def is_primex(n):
#     """
#     Assumes that n is a positive natural number
#     """
#     # We know 1 is not a prime number
#     if n <= 1:
#         return False

#     i = 2
#     # This will loop from 2 to int(sqrt(x))
#     while i*i <= n:
#         # Check if i divides x without leaving a remainder
#         if n % i == 0:
#             # This means that n has a factor in between 2 and sqrt(n)
#             # So it is not a prime number
#             return False
#         i += 1
#     # If we did not find any factor in the above loop,
#     # then n is a prime number
#     return True
    


# TESTING AND DEBUGGING

# # arr = [x for x in range(100) if prime(x)]
# print( [x for x in range(10000) if is_prime(x)]==[x for x in range(10000) if prime(x)] )
# print( [x for x in range(10000) if is_prime(x)]==[x for x in range(10000) if is_primex(x)] )
# for i in range(100):
#     print(i, end=", ") if is_prime(i) else None

# check = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# for i in check:
#     print(i) if prime(i) else None
    
## DEBUGGING TOOL
# def prime(num):
#     if num > 1:
#         for i in range(2, int(num/2)+1):
#             if (num % i) == 0:
#                 return False
#         else:
#             return True
#     else:
#         return False




# print( [x for x in range(1000) if is_prime(x)]==[x for x in range(1000) if prime(x)] )

# DEBUGGING TOOL
# def prime(num):
#     if num > 1:
#         for i in range(2, int(num/2)+1):
#             if (num % i) == 0:
#                 return False
#         else:
#             return True
#     else:
#         return False
print()
