

# Two Even Kilos
# Have to find two different divisors whose sum are equal to given digit

divisors = []
vaag_hobe = 0
weight = int(input())
for i in range(2, weight, 2):
    divisors.append(i)

for i in divisors:
    for j in divisors:
        vaag_hobe += 1 if i+j == weight else 0

print("YES") if vaag_hobe else print("NO")

# print(divisors)