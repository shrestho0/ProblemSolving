


# # # Learning Part
# # from itertools import combinations

# # print(list(combinations('12345', 2)))
# # print(list(combinations([1,1,3,3,3], 4)))










# # Solution 
# from itertools import combinations

# def check_type(string):
#     try: return int(string)
#     except: return string

# # n,k = map(check_type, input().split())
# n, k = "HACK", 2
# combinations_x = []

# for i in range(1,k+1):
#     combinations_x += sorted(combinations(n,i))

# for j in combinations_x: print(*sorted(j), sep="")


# # A
# # C
# # H
# # K

# # AC
# # AH*
# # AK
# # CK
# # HA
# # HC
# # HK

# # print(sorted(list(combinations("HACK", 2))))



from itertools import combinations
def check_type(string):
    try: return int(string)
    except: return string

n,k = map(check_type, input().split())

for _ in range(1,k+1):
    x = []
    for __ in sorted(list(combinations(n, _))):
        x.append("".join(sorted(__)))

    print(*sorted(x),sep="\n")
