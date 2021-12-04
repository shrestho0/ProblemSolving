


def less_or_equal():
    n, k = map(int, input().split())
    arr = tuple(sorted(map(int, input().split())))
    show = -1

    if k == 0:
        return arr[0]-1 if arr[0] > 1 else -1

    if k==n: return arr[n-1]

    return -1 if arr[k-1] == arr[k] else arr[k-1]


print(less_or_equal())