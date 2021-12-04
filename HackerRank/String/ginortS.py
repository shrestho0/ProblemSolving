



string = input()
lower = tuple(sorted(x for x in string if x.islower()))
upper = tuple(sorted(x for x in string if x.isupper()))
__odd = tuple(sorted(x for x in string if x.isnumeric() and not int(x)%2==0 ))
_even = tuple(sorted(x for x in string if x.isnumeric() and int(x)%2==0 ))
print(''.join(lower+upper+ __odd+ _even))