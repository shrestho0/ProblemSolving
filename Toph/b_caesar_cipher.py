


# def caesar_cipher(n, msg):
#     char_list = []
#     for char in msg:
#         if char >= 'a' and char <= 'z':
#             new_char_ascii = ord(char) - n
#             if new_char_ascii < 97 or new_char_ascii > 122:
#                 new_char_ascii = ord(char) - n + 26
#                 char_list.append(chr(new_char_ascii))
#             else:
#                 char_list.append(chr(new_char_ascii))

#         elif char >= 'A' and char <= 'Z':
#             new_char_ascii = ord(char) - n
#             if new_char_ascii < 65 or new_char_ascii > 90:
#                 new_char_ascii = ord(char) - n + 26
#                 char_list.append(chr(new_char_ascii))
#             else:
#                 char_list.append(chr(new_char_ascii))


#         else:
#             char_list.append(char)

#     return "".join(char_list)



# print(caesar_cipher(int(input()), input()))
# # print(caesar_cipher(2, "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()))

# # for _ in range(28):
# #     print(caesar_cipher(_, "hello, world"))




# def cypher(num, word):
#     s = ''
#     for x in word:
#         if ord(x.lower()) < 123 and ord(x.lower()) > 96:
#             if ord(x)-num < 97:
#                 z = chr((ord(x)-num)+26)
#             else:
#                 z = chr(ord(x)-num)
#             if x.isupper():
#                 s += z.upper()
#             else: s+= z
#         else:
#             s += x
#     return s
# print(cypher(int(input()),input()))