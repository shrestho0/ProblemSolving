

input() # dhudvat
string = input().strip()

dicto = {}

for i in range(0, len(string)-1):
    new_sting = string[i]+string[i+1]
    
    if new_sting not in dicto:
        dicto[new_sting] = 1
    else: dicto[new_sting] += 1

print(sorted(dicto.items(), key=lambda x: x[1], reverse=True)[0][0])