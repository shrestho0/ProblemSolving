








f=lambda n:  "FizzBuzz" if n%3 == 0 and n%5==0 else "Buzz" if n%5 ==0 else "Fizz" if n% 3 == 0 else n
print(*[f(x) for x in range(1,101)])

print()
x = map(lambda n:  "FizzBuzz" if n%3 == 0 and n%5==0 else "Buzz" if n%5 ==0 else "Fizz" if n% 3 == 0 else n, range(1,101))
print(*list(map(lambda n:  "FizzBuzz" if n%3 == 0 and n%5==0 else "Buzz" if n%5 ==0 else "Fizz" if n% 3 == 0 else n, range(1,101))),sep="\n")


for x in range(1,101):print("Fizz"*(x%3==0)+(x%5==0)*"Buzz"or x)

# print(*list(map(lambda n:"FizzBuzz"if n%15==0else"Buzz"if n%5==0else"Fizz"if n%3==0else n,range(1,101))),sep="\n")
