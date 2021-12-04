




def decent_arrays(n, arr:list) -> str:
    arr_len = len(arr)
    if arr_len != n: return "No"
    check_arr = all([ arr[i]<=arr[i+1] for i in range(arr_len-1) ])
    
    return "Yes" if check_arr else "No"


print(decent_arrays(int(input()), list(map(int, input().split()))))