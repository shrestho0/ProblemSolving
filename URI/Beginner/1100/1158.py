



for _ in range(int(input())):
    from_n, untill = map(int, input().split())
    print(sum([x for x in range(from_n, (from_n+(2*untill))) if x%2!=0]))
    