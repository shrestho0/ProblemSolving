


#@ LEARNING

from collections import OrderedDict

dicto = {}
dicto['a'] = 1
dicto['b'] = 2
dicto['c'] = 3
dicto['d'] = 4
dicto['e'] = 5
print(dicto)

odicto = OrderedDict()
odicto['a'] = 1
odicto['c'] = 3
odicto['b'] = 2
odicto['d'] = 4
odicto['e'] = 5
print(odicto)
print('#@==============================================@#')







#@TAKS



# items = OrderedDict()
# items['FRIES'] = 12
# items['FRIES'] += 12
# print(items)
# print('FRIES' in items)

stock = OrderedDict()
for i in range(int(input())):
    item = input().split()
    name,cost = ' '.join(item[:-1]), int(item[-1])
    if name not in stock:
        stock[name] = cost
    else:
        stock[name] += cost

for x, y in stock.items():
    print(x,y)
