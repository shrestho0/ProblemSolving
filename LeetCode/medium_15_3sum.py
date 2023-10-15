


def threeSum(nums):
    results = []
    nums.sort()
    
    nums_len = len(nums)
    for i, el in enumerate(nums):
        if i > 0 and nums[i-1] == el:
            continue
 
        exl = i+1
        exr = nums_len - 1
        while exl < exr: 
            
            xxsum = el + nums[exl] + nums[exr]
            
            if xxsum < 0:
                exl += 1
            elif xxsum > 0: 
                exr -= 1
            elif xxsum == 0:
                results.append( [i, exl, exr] )
                exl += 1
                while nums[exl] == nums[exl-1] and exl < exr:
                    exl += 1 
    
    return results
 


a = [-1,0,1,2,-1,-4] # [[-1,-1,2],[-1,0,1]]
b = [0,1,1] # []
c = [0,0,0] # [0,0,0]

print(threeSum(a))
print(threeSum(b))
print(threeSum(c))