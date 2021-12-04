

def solve(s):
    
    f_string = ''
    for i in range(len(s)-1):
        if i == 0: f_string+= s[i].capitalize()
        if s[i] == ' ' or s[i] == '': f_string += s[i+1].capitalize()
        else: f_string += s[i+1]

    return f_string
    # for i in 
    # return s.title()


# print(solve(input()))
print(solve("chris alan"))
print(solve('1 w 2 r 3g'))
