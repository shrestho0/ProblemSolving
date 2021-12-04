





n,m = tuple((int(x) for x in input().split()))
athletes = []
for _ in range(n):
    ath = tuple((int(x) for x in input().split()))
    athletes.append(ath) if len(ath) > 2 else None
key = int(input())


for ath in sorted(athletes, key=lambda x: x[key]):
    print(*ath)

