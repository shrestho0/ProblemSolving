

#DS
#Reversed array

# way01
# def reversed_array(arr):
#     return [arr[x] for x in range(len(arr)-1,-1,-1)]


# n = input()
# arr = tuple(map(int, input().split()))
# print(*reversed_array(arr))

# way02
def reversed_array(a):
    arr = []
    for i in range(len(a)-1, -1, -1):
        arr.append(a[i])
    return arr

n = input()
arr = tuple(map(int, input().split()))
print(reversed_array(arr))

