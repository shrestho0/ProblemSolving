


output = []
for i in range(int(input())):
    string = input()
    if len(string) > 10:
        output.append(f"{string[0]}{len(string[1:-1])}{string[-1]}")
    else:
        output.append(string)

print(*output, sep="\n")