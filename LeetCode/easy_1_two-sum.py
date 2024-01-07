

def twoSum(nums, target):
    checkHashTable = {}
    for i, el in enumerate(nums):        
        diff= target - el
        if diff in checkHashTable:
            return [checkHashTable[diff], i]
        checkHashTable[el] = i 


for x in ( ([2,7,11,15], 9 ), ([3,2,4], 6), ([3,3], 6) ):
    print(twoSum(*x))