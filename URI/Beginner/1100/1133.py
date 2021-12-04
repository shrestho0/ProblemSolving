




X,Y = sorted((int(input()), int(input())))
print(*(x for x in range(X+1,Y) if x%5 ==3 or x%5==2), sep="\n")

