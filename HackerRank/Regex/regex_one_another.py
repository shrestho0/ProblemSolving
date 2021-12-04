
import re
result = ''
for i in range(int(input())):
    number = input()
    pattern = re.search(r"^[789]\d{9}$", number)

    if pattern:
        result += 'Yes\n'
    else:
        result += 'No\n'

for re in result.split("\n"):
    print(re)

# if pattern:
    # print("Yes")
# else:
    # print("No")