class Solution:
    def shortestPalindrome(self, s: str) -> str:
        string = "".join(s.split())
        ulta_string = string[::-1]
        lenx = len(string)
        i = 0
        while True:
            new_string = ulta_string[0:i] + string
            if new_string == new_string[::-1]: return new_string
            i+=1


        

print(Solution().shortestPalindrome("aacecaaa"))
print(Solution().shortestPalindrome("abcd"))

# string = "aacecaaa"
# print(
#     string[::-1][0:1] + string
# )