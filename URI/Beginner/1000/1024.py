



def left_shift_string(string: str) -> str:
    return "".join( [chr(ord(x)-1) for x in string] )


print(left_shift_string("Texto #3"))
print(left_shift_string("abcABC1"))