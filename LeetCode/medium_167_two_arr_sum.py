def twoSum(arr, target):
    foundSomething = False

    i = 0 
    j = len(arr)-1

    while i < j:
        tSum = arr[i] + arr[j]
        if tSum == target:
            foundSomething = True
            break
        elif tSum < target:
            i += 1
        elif tSum > target:
            j -= 1
    return (i+1, j+1) if foundSomething else -1

print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))
print(twoSum([-1,0], -1))