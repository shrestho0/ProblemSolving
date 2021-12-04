class Solution:
    def isPalindrome(self, x: int):
        if x < 0: return False
        x = str(x)
        return True if x == x[::-1] else False

print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(121))
print(Solution().isPalindrome(123))