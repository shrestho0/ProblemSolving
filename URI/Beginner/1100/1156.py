


'''
S = 1/1 + 3/2 + 5/4 + 7/8 + ... + 39/?
'''

fucking_result = 0
upor = [x for x in range(1, 40, 2)]

nich = [2**x for x in range(len(upor))]
for x,y in zip(upor,nich):
    fucking_result+= x/y

print(f"{fucking_result:.2f}")
