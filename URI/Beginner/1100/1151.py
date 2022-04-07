

# def till_nth_fib(n):
#     if n == 0: return 0
#     if n == 1: return 1
#     return till_nth_fib(n-1) + till_nth_fib(n-2)

def till_nth_fib(n):
    listo = []
    a_0 = 0
    a_1 = 1
    
    for i in range(n):
        
        listo.append(a_0)
        
        temp =  a_0 + a_1
        a_0 = a_1
        a_1 = temp

    return listo

print(*till_nth_fib(int(input())))
print()



# print(*[till_nth_fib(x) for x in range(int(input()))])
