


# import sympy


# print("Prime") if sympy.isprime(10) else print("Not prime")

# # This performed great but time limit exeeced
# def isprime(n):
#     if n < 2: return False
#     if n == 2: return True
#     for i in range(2, n//2+1):
#         if n % i == 0:
#             return False
#             break
#     return True
# for _ in range(int(input())): print("Prime") if isprime(int(input())) else print("Not prime")


# This was far better
import math

def isPrime(n):
    if n == 2:
        return True
    elif n == 1 or (n & 1) == 0:
        return False
        
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    
    return True

p = int(input())
for i in range(0, p):
    x = int(input())

    s = "Prime" if (isPrime(x)) else "Not prime"
    print(s)
