


# Worked but time limit exited
# all_words = []
# dis_words = []
# for i in range(int(input())):
#     word = input()
#     all_words.append(word)
#     if word not in dis_words:
#         dis_words.append(word)

# # print(all_words)
# print(len(dis_words))
# for word in dis_words:
#     print(all_words.count(word), end=" ")

# all_words = []
# dis_words = []
# for i in range(int(input())):
#     word = input()
#     all_words.append(word)
#     if word not in dis_words:
#         dis_words.append(word)

# # print(all_words)
# print(len(dis_words))
# for word in dis_words:
# #     print(all_words.count(word), end=" ")
# import sys

# print(all_word)


# lines = sys.stdin.readlines()
# lines = [line for line in sys.stdin]
# print(lines)


from collections import OrderedDict

words = OrderedDict()
for i in range(int(input())): 
    word = input()
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1
print(len(set(words.keys())))
print(*words.values())