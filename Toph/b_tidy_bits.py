



n = int(input())
n_bin = bin(n).count('1')
for i in range(n):
    if bin(i).count('1') == n_bin:
        print(i)
        break
