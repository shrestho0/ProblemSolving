class Solution:
    def twoSum(self, nums, target):
        self.len = len(nums)
        
        if self.len == 2 and nums[0] + nums[1] == target: return [0,1]

        for i in range(self.len):
            for j in range(i+1, self.len):
                indic = [i,j]
                if nums[i] + nums[j] == target:
                    return indic
                

print(Solution().twoSum([3,2,3], 6))
print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([3,3], 6))
