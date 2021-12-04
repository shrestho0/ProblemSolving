
import time
import sympy


def check_prime_basic(n):
    if n < 2:
        return False
    if n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False
            break
    return True

basic_t1 = time.time()
def print_primes_basic(n=100):
    return [x for x in range(n) if check_prime_basic(x)]
basic_t2 = time.time()


sympy_t1 = time.time()
def print_prime_sympy(n=100):
    return [x for x in range(n) if sympy.isprime(x)]
sympy_t2 = time.time()


print('Basic')
print_primes_basic(100000)
print(f'Start time: {basic_t1} s\nEnd time: {basic_t2} s\nTotal exec time: {(basic_t2-basic_t1)} ms')
# print('Sympy')
# print_prime_sympy(1000)
# print(f'Start time: {sympy_t1} s\nEnd time: {sympy_t2} s\nTotal exec time: {(sympy_t2-sympy_t1)*1000} ms')
# # print()
# print_primes()

# prime_numbers_basic = [x for x in range(100) if check_prime_basic(x)]
# prime_numbers_sympy = [x for x in range(100) if sympy.isprime(x)]
