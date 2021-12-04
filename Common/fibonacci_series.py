


# Fibonacci Series Short Version
# Author: Shrestho
# Author URI: https://shrestho.me

def fibonacci_series(n: int) -> list:
    arr, n1, n2 = [], 0, 1
    while n != 0:
        arr.append(n1)
        n1, n2 = n2, n1+n2
        n -= 1
    return arr

print(*fibonacci_series(10))