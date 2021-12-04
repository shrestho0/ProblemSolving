

# def dec_to_bin(n):
#     return bin(n).replace("0b", '')
# def dec_to_oct(n):
#     return oct(n).replace('0o', '')
# def dec_to_hex(n):
#     return hex(n).replace('0x', '').upper()


# for i in range(1, int(input())+1):
#     print(f"{str(i).rjust(5)} {str(dec_to_oct(i)).rjust(5)} {str(dec_to_hex(i).rjust(5))} {str(dec_to_bin(i).rjust(5))}")




# for i in range(1, num+1): print(f"{str(i).rjust(5)} {oct(i).replace('0o', '').rjust(5)} {hex(i).replace('0x', '').rjust(5)} {bin(i).replace('0b', '').rjust(5)}")


# def print_formatted(number):
#     listo = []
#     for i in range(1, number+1):
#         listo.append([str(i), oct(i).replace('0o', ''), hex(i).replace('0x', '').upper(), bin(i).replace('0b', '')])

#     w = len(str(listo[-1][3]))
#     for _ in listo: 
#         print(*(x.rjust(w) for x in _))


# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)


# def print_formatted(n):
#     for i in range(1,n + 1):
#         pad = n.bit_length()
#         print(f'{i:{pad}d} {i:{pad}o} {i:{pad}X} {i:{pad}b}')

# print_formatted(17)
number = 17
for i in range(number):
    space = number.bit_length()
    print(f'{i:{space}d} {i:{space}o} {i:{space}X} {i:{space}b}')