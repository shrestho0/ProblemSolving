





string  = ""
for _ in range(1000000):
    get_bal = input()
    if get_bal == "\b": break
    try:
        start,end = map(int, get_bal.split())
    except ValueError:
        break

    def find_n(n):
        result = 0
        while True:
            result+=1
            if n==1: break
            if n % 2 == 1:
                n = 3*n +1
            else:
                n //= 2
        return result

    lenx = 0
    for i in range(start, end):
        x = find_n(i)
        if x> lenx:
            lenx=x

    string+= f"{start} {end} {lenx}\n"


print(string)
    


