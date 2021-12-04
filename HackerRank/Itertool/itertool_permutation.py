
## Learning
# from itertools import permutations

# print(permutations([1,2,3]))
# print(list(permutations([1,2,3])))
# print(list(permutations([1,2,3],2)))
# print(list(permutations(['a','b','c'],3)))




# Solution
from itertools import permutations
def check_type(string):
    try: return int(string)
    except: return string

n,k = map(check_type, input().split())

for _ in sorted(permutations(n,k)): print(*_, sep="")