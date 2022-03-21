get_sides = input().split()
A, B = (float(x) for x in get_sides)

if A % B == 0 or B % A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

