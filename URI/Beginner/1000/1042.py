# Accepted on first chance but a compilation error
get_nums = input().split()
get_nums = [int(x) for x in get_nums]
get_sort = sorted(get_nums)

for el in get_sort:
    print(el)
print()
for el in get_nums:
    print(el)
    