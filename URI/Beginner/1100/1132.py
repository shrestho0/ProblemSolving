


X,Y = sorted((int(input()), int(input())))
print(sum( (x for x in range(X,Y+1) if x%13 != 0) ))