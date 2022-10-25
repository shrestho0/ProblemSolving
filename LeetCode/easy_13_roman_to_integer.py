"""
https://leetcode.com/problems/roman-to-integer/
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        alpha = 'IVXLCDM'
        numer = [1, 5, 10, 50, 100, 500, 1000]
        value = sum(numer[alpha.index(char)] for char in s)

        for i in range(len(s)-1):
            char, n_char = s[i], s[i+1]
            if char == "I" and n_char in "VX":
                value -= 2
            elif char == "X" and n_char in "LC":
                value -= 20
            elif char == "C" and n_char in "DM":
                value -= 200

        return value


test_case = Solution()

test_case.romanToInt("III")
test_case.romanToInt("LVIII")
test_case.romanToInt("MCMXCIV")
test_case.romanToInt("XXVII")
test_case.romanToInt("II")