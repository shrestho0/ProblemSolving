




def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print(str(factorial(int(input())))[-4:])
# print(str(numpy.math.factorial(int(input())))[-4:])