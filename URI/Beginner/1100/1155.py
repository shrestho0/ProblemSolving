'''


S = 1 + 1/2 + 1/3 + … + 1/100

'''

fucking_result = 0
for i in range(1, 101):
    fucking_result+= 1/i

print(f"{fucking_result:.2f}")