
'''
https://leetcode.com/problems/longest-common-prefix/
'''
from typing import List

class Solution:
    def longestCommonPrefixUtil(self, str_one, str_two):
        i,j = 0,0
        com = ""
        while i < len(str_one) and j < len(str_two):
            if str_one[i] != str_two[j]:
                break
            com += str_one[i]
            i,j = i+1, j+1
        return com

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1: return ""
        if len(strs) == 1: return strs[0]

        com = self.longestCommonPrefixUtil(strs[0], strs[1])
        for i in range(1, len(strs)):
            com = self.longestCommonPrefixUtil(com,strs[i])
        return com

t1 = Solution()
print(t1.longestCommonPrefix(["flower", "flow", "flight"]))
print(t1.longestCommonPrefix(["dog", "racecar", "car"]))