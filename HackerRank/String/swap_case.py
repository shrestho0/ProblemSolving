def swap_case(s):
    swap = ''
    
    for _ in s:
        if _.isupper(): swap += _.lower()
        elif _.islower(): swap += _.upper()
        else: swap += _

    return swap
        

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)