import textwrap

def wrap(string, max_width):  
    result = ''
    wrapper = textwrap.TextWrapper(width=max_width)
    for _ in wrapper.wrap(string): result+= _+'\n'
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)




# # Check how wrapper works

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# wrapper = textwrap.TextWrapper(width = 4)
# for _ in wrapper.wrap(text=string):
#     print(_)