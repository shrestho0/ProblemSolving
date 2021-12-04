




# A, B = [], []
# for i in range(2): A.append(list(map(int, input().split())))
# for i in range(2): B.append(list(map(int, input().split())))


# print(A)
# print(B)

def matrix_mul_2D(A, B):
    C11 = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    C12 = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    C21 = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    C22 = A[1][0] * B[0][1] + A[1][1] * B[1][1]


    print(C11, C12); print(C21, C22)

    

A = [ list(map(int, input().split())) for _ in range(2) ]
B = [ list(map(int, input().split())) for _ in range(2) ]
matrix_mul_2D(A,B)