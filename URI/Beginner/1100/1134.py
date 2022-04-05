






'''

coded as follows: 1. Alcohol 2. Gasoline 3. Diesel 4. End

'''
print("MUITO OBRIGADO")
fuels = [0, 0, 0]
while True:
    k = int(input())
    if k == 4: break
    if k in range(1,4): fuels[k-1] += 1

print(f"Alcool: {fuels[0]}")
print(f"Gasolina: {fuels[1]}")
print(f"Diesel: {fuels[2]}")


