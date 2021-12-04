


every_thing = []
n, m = map(int, input().split())
for _ in range(n):
    every_thing.append(input())
word_list = []
for i in range(m):
    srt = ''
    for x in every_thing:
        char = x[i]
        if char.isalnum():
            srt += char
        else:
            srt += '-'
    word_list.append(srt)
    print()


print(word_list)
print()