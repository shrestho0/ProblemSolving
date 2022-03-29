










def fair_distribution(X,Y):
    return X - (Y % X)



print(fair_distribution(*map(int, input().split())))


