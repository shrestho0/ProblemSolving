


strings, queries = [], []
for _ in range(int(input())): strings.append(input())
for _ in range(int(input())): queries.append(input())
for q in queries:
    print(strings.count(q))
