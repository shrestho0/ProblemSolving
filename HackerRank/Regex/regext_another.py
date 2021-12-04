
import re
code = """
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
"""
code = "x&& &&& && && x || | ||\|| x"
# pip = "(\s\|\|\s)"
# amp = "(\s\&\&\s)"
# code = re.sub(amp," and ",code)
# code = re.sub(pip," or ",code)
# print(code)
import re
get_line =int(input())
for i in range(get_line):
      amp=re.compile(r'(?<= )(&&)(?= )')
      pip=re.compile(r'(?<= )(\|\|)(?= )')
      print(pip.sub('or', amp.sub('and', input())))