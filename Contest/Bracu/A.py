




def fizzbuzz(n):
    if n % 2 == 0 and n % 5 == 0:
        return "fizzbuzz"
    else:
        if n % 2 == 0:
            return "fizz"
        elif n % 5 == 0:
            return "buzz"
        else:
            return "sad"

print(fizzbuzz(int(input())))