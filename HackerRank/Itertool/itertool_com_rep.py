print(*["AA", "AC", "AH", "AK", "CC", "CH", "CK", "HH", "HK", "KK"])

from itertools import combinations_with_replacement

def convert_type(string):
    try: return int(string)
    except: return string

# n, k = map(convert_type, input().split())
n, k = "HACK", 2

com_x = []
for _ in sorted(list(combinations_with_replacement(n, k))):
    com_x.append(sorted(_))

for _ in sorted(com_x): print(*_, sep="")
