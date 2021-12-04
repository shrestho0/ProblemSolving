

# pyridamid = '''
#   *
#  * *
# * * *
# '''

# print(pyridamid.split('\n')[1:-1])


pyr_list = []

n = int(input())
for i in range(1, n+1):
    pyr_list.append(' '*(n-i) + " ".join(['*']*i))

string = "\n".join(pyr_list)
print(string)
