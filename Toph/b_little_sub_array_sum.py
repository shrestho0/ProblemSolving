



def little_sub_array(n, from_idx, to_idx, arr: list):
    return sum([arr[idx] for idx in range(from_idx, to_idx+1)])

print(little_sub_array(*map(int, input().split()), list(map(int, input().split()))))