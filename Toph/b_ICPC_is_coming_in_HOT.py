





def highest_freq(number: str):
    return sorted({x:number.count(x) for x in sorted(set(number))}.items(), key=lambda x: x[1], reverse=True)[0][0]

print(highest_freq(input()))