# Accepted on first attempt, Alhamdulillah 

get_sides = input().split()
A, B, C = (float(x) for x in get_sides)

if (A+B > C) and (B+C > A) and (C+A) > B:
    print(f"Perimetro = {(A+B+C):.1f}")
else:
    print(f"Area = {(((A+B)/2)*C):.1f}") 


