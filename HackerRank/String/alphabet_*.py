


import string
let = string.ascii_lowercase




# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# # i * 4 - 3
# print('----3----', len('----c----'))
# print('--------5--------', len('--------e--------'))
# print('------------------10------------------', len('-------------

n = 5
m = 4*n-3

for i in range(n-1, -n, -1):
    if i >= 0:
        letX = "-".join(let[i:n])
        letX = letX[::-1] + letX[1:]
        print(letX.center(m, '-'))
    else:
        letY = "-".join(let[n-1:-i-1:-1])
        letY = letY[:-1] + letY[::-1]
        print(letY.center(m, '-'))



# listxx = ['I', 'hate', 'Java']
# string = '-'.join(listxx)
# print(string)