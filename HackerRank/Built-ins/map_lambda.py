


# #LEARNING PART
# print (list(map(len, ['Tina', 'Raj', 'Tom'])))  
# sumx = lambda a,b,c : a+b+c
# print(sumx(19,11,20))


#@ TAKS
## n-th fib number's cube

# PART01 -  Fibonacci Generator

def fibonacci_list(n):
    arr = []
    n1 = 0
    n2 = 1
    while n != 0:
        arr.append(n1)

        n1, n2 = n2, n1+n2
        n -= 1
    return arr

print(list(map(lambda x: x**3, fibonacci_list(int(input())))))
        
