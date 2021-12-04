
s = "qA2"
# s = "^^^"

# is_alnum, is_alpha, is_digit, is_lower, is_upper = (None for _ in range(5))

# for _ in s:
#     if _.isalnum(): is_alnum*= True


    

# print(is_alnum, is_alpha)

methods = ["isalnum", "isalpha", "isdigit", "islower", "isupper"]

for _ in methods:
    print(eval(f"any(c.{_}() for c in s)"))
# print(any(c.isalnum() for c in s))

