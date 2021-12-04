

# Fibonacci
def fibonacci(limit=10000000000):
  listx = []
  prev_one, memory, fibonacci = 0, 0, 1
  for i in range(limit+1):
    prev_one = fibonacci
    fibonacci = memory
    memory = prev_one + fibonacci
    if fibonacci > limit:
      break
    listx.append(fibonacci)
  return listx

print(fibonacci()[int(input())])

# print(fibonacci(int(input())))

# fibonacci(50)
# fibonacci(5)

# for i in range(50+1):
#     if fibonacci(i):
#         print(fibonacci(i))

# print(fibonacci(10000000000))



