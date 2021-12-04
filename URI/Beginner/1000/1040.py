# Accepted in first attempt
# A bit tough to understand the language
get_nums = input()
N1, N2, N3, N4 = (float(x) for x in get_nums.split(' '))

avg = (N1*2 + N2*3 + N3*4 +N4*1 ) / 10
print(f"Media: {avg:.1f}")
if avg >= 7.0:
    print("Aluno aprovado.")
elif avg < 5.0:
    print("Aluno reprovado.")
elif avg >= 5.0 and avg <= 6.9:
    print("Aluno em exame.")
    N5 = float(input())
    print(f"Nota do exame: {N5}")
    avg = (avg+N5 )/2
    if avg >= 5.0:
        print("Aluno aprovado.")
        print("Media final:", avg)
    elif avg <= 4.9:
        print("Aluno reprovado.")
        print("Media final:", avg)
