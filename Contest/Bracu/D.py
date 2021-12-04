



# cf_types = (2,4,8,16, 32)
# cf_split = 2

# get_file = tuple(map(int, input().split()))
# c_lagbe = 


# civit_ache = sum([(cf_types[i] * get_file[i])//2 for i in range(5)])
# dite_parbe = civit_ache - c_lagbe

# if dite_parbe >= c_lagbe:
#     print("Yes")
# else:
#     print("No")


def ceevit_hobe(pack_hobe, lagbe):
    if lagbe % 2 != 0: return "No"
    lagbe //= 2
    ceevit_pack = (2,4,8,16,32)
    ceevit_hobe = sum([x*y for x,y in zip(pack_hobe, ceevit_pack)])//2

    return "YES" if ceevit_hobe > lagbe else "NO"

print(ceevit_hobe(tuple(map(int, input().split())), int(input())))
