# # def get_first_last_digits(string):
# #     first, last = None, None
# #     l, r = 0, len(string) - 1
# #     while True:
# #         if not first and string[l].isdigit():
# #             first = string[l]
# #         if not last and string[r].isdigit():
# #             last = string[r]
# #         if first and last:
# #             break
# #         l += 1
# #         r -= 1

# #     return int(first + last)


# with open("src/input4.txt", "r") as f:
#     num_words = ["nine", "eight", "seven", "six", "five", "four", "three", "two", "one"]
#     num_digit = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]
#     digits_arr = []
#     for line in f.readlines():
#         digits = ""
#         line = line.strip()

#         j = 0
#         while j < len(line):
#             word = ""
#             if line[j].isnumeric():
#                 digits += line[j]
#                 j += 1
#             for k in range(5):
#                 if k < 2:
#                     continue
#                 if j + k > len(line):
#                     continue

#                 word = line[j : j + k + 1]
#                 if word in num_words:
#                     # line = (
#                     #     line[:j] + num_digit[num_words.index(word)] + line[j + k + 1 :]
#                     # )
#                     # print(word, num_digit[num_words.index(word)])
#                     digits += num_digit[num_words.index(word)]

#             j += 1
#         digits_arr.append(digits)

#     def twodigit(string):
#         if len(string) == 1:
#             return int(string + string)
#         return int(string[0] + string[len(string) - 1])

#     digits_arr = list(map(twodigit, digits_arr))
#     print(digits_arr, sum(digits_arr))
# #     lines = f.readlines()
# #     val = [get_first_last_digits(line.strip()) for line in lines]
# #     print(val, sum(val))


num_words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_number(dstr):
    dlen = len(dstr)
    d_only_str = ""
    for i, char in enumerate(dstr):
        if char.isdigit():
            d_only_str += char
            continue
        for j in range(2, 5):
            if i + j < dlen:
                word = dstr[i : i + j + 1]
                if word in num_words:
                    d_only_str += str(num_words[word])
                    continue

    if (dslen := len(d_only_str)) == 1:
        return int(f"{d_only_str[0]*2}")

    return int(f"{d_only_str[0]}{d_only_str[dslen - 1]}")


with open("input4.txt", "r") as f:
    sum_dstr = 0
    for line in f.readlines():
        sum_dstr += get_number(line.strip())
    print(sum_dstr)
