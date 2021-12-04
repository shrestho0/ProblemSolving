


def printH(n):
    for i in range(1, n+1):

        if n % 2 == 0:
            if (i == n//2) or (i == n//2+1): print('*'*5)
            else: print("*" + '-'*3 + "*")
        else:
            if i == n//2+1: print('*'*5)
            else: print("*" + '-'*3 + "*")


printH(5), print(), printH(6), print(), printH(7)