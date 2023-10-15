def containsDuplicate(nums):
    
    
    num_len = len(nums)
    nums.sort()

    for i,el in enumerate(nums):
        if i>0 and el == nums[i-1]:
            return True
        
    return False


a, b, c = [1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(a))
print(containsDuplicate(b))
print(containsDuplicate(c))