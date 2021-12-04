# # ------------.|.------------ 12 + 3  + 12
# # ---------.|..|..|.--------- 9  + 9  +  9
# # ------.|..|..|..|..|.------ 6  + 15 + 6
# # ---.|..|..|..|..|..|..|.--- 3  + 21 + 3
# # ----------WELCOME---------- 9  + 9  + 9
# # ---.|..|..|..|..|..|..|.--- 3  + 21 + 3
# # ------.|..|..|..|..|.------ 6  + 15 + 6
# # ---------.|..|..|.--------- 9  + 9  + 9
# # ------------.|.------------ 12 + 3  +12
n, m = 9, 27

# hyp: int = None
# mid: int = None
# # mid = None

# for i in range(1, n+1):
    # if i > n//2+1:
    #     hyp = 3 * (n//2 - (n-i))
    # elif i == n//2+1:
    #     hyp = n
    # elif i < n//2+1:
    #     hyp = 3 * (n//2 - i+1)
    # else:
    #     continue

    # if i > n//2+1:
    #     if i % 2 == 0: mid =f"{hyp//3} Jor, Beshi"
    #     else: mid = f"{hyp//3} Bejor, Beshi."
    # elif i == n//2+1:
    #     mid = n
    # elif i < n//2+1:
    #     if i % 2 == 0: mid ="Jor, Kom"
    #     else: mid = "Bejor, Kom."
    # else:
    #     continue


for i in range(1, n, 2): print((i*'.|.').center(m, '-'))
print('WELCOME'.center(m, '-'))
for i in range(n-2, 0, -2): print((i*'.|.').center(m, '-'))


    



#     print('-'*hyp, mid,  '-'*hyp)


# N, M = map(int,input().split())
# for i in range(1,N,2): 
#     print((i * ".|.").center(M, "-"))
# print("WELCOME".center(M,"-"))
# for i in range(N-2,-1,-2): 
#     print((i * ".|.").center(M, "-"))