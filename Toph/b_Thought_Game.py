


# from math import floor as ceil

string_list = [] 
for i in range(int(input())):
    if int(sum((int(x) for x in input().split())) / 2) % 2 == 0:
        string_list.append("Sadia will be happy.")
    else: string_list.append("Oops!")



print(*string_list, sep="\n")

# Sadia will be happy.