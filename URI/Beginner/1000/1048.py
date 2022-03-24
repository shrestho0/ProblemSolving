# Worked after 2 attempts
# One was percentage had floating value
# Presentation Error.
# And, Alhamdulillah did it successfully
# 0 - 400.00        15%
# 400.01 - 800.00   12%
# 800.01 - 1200.00  10%
# 1200.01 - 2000.00 7%
# Above 2000.00     4%


sal = float(input())

# new_saly, new_earn, new_perc = 0, 0, 0, 0

if sal >= 0 and sal <= 400:
    new_perc = 15
elif sal >= 400.01 and sal <= 800.00:
    new_perc = 12
elif sal >= 800.01 and sal <= 1200.00:
    new_perc = 10

elif sal >= 1200.01 and sal <= 2000.00:
    new_perc = 7
elif sal > 200:
    new_perc = 4


new_earn = sal * new_perc/100
new_saly = sal + (sal * new_perc/100)

print(f"Novo salario: {new_saly:.2f}")
print(f"Reajuste ganho: {new_earn:.2f}")
print(f"Em percentual: {new_perc} %")



