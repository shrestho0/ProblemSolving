# Accepted in first attempt, Alhamdulillah 
get_sides = input().split()
get_sides = sorted([float(x) for x in get_sides], reverse=True)
A, B, C = (float(x) for x in get_sides)

if (A > 0 and B > 0 and C > 0):
    # if A ≥ B + C, write the message: NAO FORMA TRIANGULO
    if A >= B + C:
        print("NAO FORMA TRIANGULO")
    # if A2 = B2 + C2, write the message: TRIANGULO RETANGULO
    elif A**2 == (B**2 + C**2):
        print("TRIANGULO RETANGULO")
    # if A2 > B2 + C2, write the message: TRIANGULO OBTUSANGULO
    elif A**2 > (B**2 + C**2):
        print("TRIANGULO OBTUSANGULO")
    # if A2 < B2 + C2, write the message: TRIANGULO ACUTANGULO
    elif A**2 < (B**2 + C**2):
        print("TRIANGULO ACUTANGULO")
    # if the three sides are the same size, write the message: TRIANGULO EQUILATERO
    if ((A+B > C) and (B+C > A) and (C+A) > B):
        if A == B and B == C:
            print("TRIANGULO EQUILATERO")
        # if only two sides are the same and the third one is different, write the message: TRIANGULO ISOSCELES
        elif A==B or B==C or C==A:
            # A == B and C != A and C != B or,
            # B == C and A != B and A != C or,
            # C == A and B != A and A != C
            print("TRIANGULO ISOSCELES")