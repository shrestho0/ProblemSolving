

def better_pass(string: str):
    first_letter = string[0].upper()
    string = string[1:]
    string = string.replace('s', '$')
    string = string.replace('i', '!')
    string = string.replace('o', '()')
    string += '.'

    return first_letter + string

print(better_pass(input()))

