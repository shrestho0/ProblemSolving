

# #@ Learning Part
# import numpy

# a = numpy.array([1,2,3,4], float)
# b = numpy.array([5,6,7,8], float)

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)

#@TASK

# import numpy
# n, m = map(int, input().split())

# for i in range(n):
#     A = numpy.array(input().split(), int)
#     B = numpy.array(input().split(), int)

#     print(numpy.array(sorted[A+B]))
#     print(numpy.array(sorted[A-B]))
#     print(numpy.array(sorted[A*B]))
#     print(numpy.array(sorted[A//B]))
#     print(numpy.array(sorted[A%B]))
    # print(numpy.array(sorted[A**B]))


# print()

# for i in range(n+1):
#     M = tuple(int(x) for x in input().split())
#     print(M)


# import numpy

# n, m = tuple(int(x) for x in input().split())
# A = numpy.array([], int)
# B = numpy.array([], int)
# for i in range(2*n):
#     a = numpy.array(input().split(), int)
#     b = numpy.array(input().split(), int)
#     numpy.append(A, a)
#     numpy.append(B, b)
#     # numpy.append(A, input().split())
#     # numpy.append(B, input().split())
#     # A.append(numpy.array(input.split(), int))
#     # B.append(numpy.array(input().split(), int))

# print(A, B)
import numpy
A, B = [], []
n, m = tuple(int(x) for x in input().split())
for _ in range(2):
    if n == 1:
        A.append(input().split())
        B.append(input().split())
        break
    else:
        if _%2 ==0:
            A.append(input().split())
            A.append(input().split())
        else:
            B.append(input().split())
            B.append(input().split())
    
A = numpy.array(A, int)
B = numpy.array(B, int)

print(A+B, A-B, A*B, A//B, A%B, A**B, sep="\n")
# for 
# print(B)
# print(n, m)
# print(A)
# print(B)