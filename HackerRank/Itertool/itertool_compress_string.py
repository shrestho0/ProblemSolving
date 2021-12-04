1222311


# import itertools

# def keyfunc(key):
#     return data.count(x)

# data = '1222311'
# groups = []
# unique_keys = []
# for item in data:
#     unique_keys.append(item) if item not in unique_keys else None
# print(unique_keys)
# # def keyfunc(key):
# #     return data.count(x)

# data = sorted(data, key=keyfunc)

# for k, g in itertools.groupby(data, keyfunc):
#     groups.append(list[g])
#     unique_keys.append(k)





# data = '1222311'

# for i in d

from itertools import groupby
data = input()
for c, items in groupby(data):
    print(tuple((len(list(items)), int(c))), end=" ")