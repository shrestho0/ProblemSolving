



# def wordPattern(pattern, string):
#     pat_string_map = {}
#     str_pattern_map = {}
    

#     if len(pattern) != len(string): return False

#     if len(pattern) == len(string):
#         for char_p, char_s in zip(pattern, string):
#             if char_s not in pat_string_map and char_p not in str_pattern_map:
#                 pat_string_map[char_s], str_pattern_map[char_p] = char_p, char_s
#             elif pat_string_map.get(char_p) == char_s and str_pattern_map.get(char_s) == char_p:
#                 pass
#             else:
#                 return False
#         return True
#     return pat_string_map, str_pattern_map
    


# pattern = "abba"
# string = "baab"
# print(wordPattern(pattern, string))





# def char_pattern(pattern, string):
#     if ' ' in string: string = string.split()
#     pattern_map, char_map = {}, {}

#     if len(pattern) != len(string): return False
#     for pat, char in zip(pattern, string):
#         if char not in pattern_map and pat not in char_map:
#             pattern_map[char], char_map[pat] = pat, char
#         elif pattern_map.get(char) == pat and char_map.get(pat) == char:
#             pass
#         else: return False

#     print(pattern_map, char_map)

#     return True


# print(char_pattern("abba", "baab"))   # True
# print(char_pattern("abc", "bcd"))     # True
# print(char_pattern("---", "***"))     # True
# print(char_pattern("abba", "dog cat cat dog"))    # True
# print(char_pattern("abba", "dog cat cat fish"))   # False
# print(char_pattern("aaaa", "dog cat cat cat"))    # False
# print(char_pattern("abba", "dog dog dog dog"))    # False



def detect_pattern(s1, s2):
    if ' ' in s2: s2 = s2.split(' ')
    pattern_map, char_map = {}, {}
    if len(s1) != len(s2): return False
    for pat, char in zip(s1, s2):
        if char not in pattern_map and pat not in char_map:
            pattern_map[char], char_map[pat] = pat, char
        elif pattern_map.get(char) == pat and char_map.get(pat) == char: pass
        else: return False
    return True







def char_pattern(pattern, string):
    if ' ' in string: string = string.split(' ')
    pattern_map, char_map = {}, {}
    if len(pattern) != len(string): return False
    for pat, char in zip(pattern, string):
        if char not in pattern_map and pat not in char_map:
            pattern_map[char], char_map[pat] = pat, char
        elif pattern_map.get(char) == pat and char_map.get(pat) == char: pass
        else: return False
    return True

    


print(char_pattern("", ""))
print(char_pattern("abba", "baab"))   # True
print(char_pattern("abc", "bcd"))     # True
print(char_pattern("------", "******"))     # True
print(char_pattern("abba", "dog cat cat dog"))    # True
print(char_pattern("abba", "dog cat cat fish"))   # False
print(char_pattern("aaaa", "dog cat cat cat"))    # False
print(char_pattern("abba", "dog dog dog dog"))    # False


