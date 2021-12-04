



def mixed_fraction(nomi, deno):
    return nomi//deno, nomi % deno, deno


print(*mixed_fraction(*map(int, input().split())))