

# def company_logo(string: str):
#     chars = []
#     for char in string: chars.append(char) if char not in chars else None
#     chars = sorted(chars)
#     charx = [] 
#     count = 0
#     for idx in range(len(chars)):
#         now_count = string.count(chars[idx])
#         if now_count > count:
#             count = now_count
#             charx.insert(0, (chars[idx], count))
#         else:
#             charx.append((chars[idx], now_count))
#     return charx[:3]

    

# company = company_logo(input())
# for c_k in company:
#     print(*c_k)




from collections import OrderedDict, Counter

class OrderedCounter(Counter, OrderedDict): pass

def company_logo(string):
    x = [c for c in OrderedCounter(sorted(string)).most_common(3)]
    return x
    
for char in company_logo(input()):
    print(*char)

