"""

UNSOLVED

https://leetcode.com/problems/integer-to-roman/

"""

class Solution:
    def intToRoman(self, num: int) -> str:
        alpha = 'IVXLCDM'[::-1]
        numer = [1, 5, 10, 50, 100, 500, 1000][::-1]
        roman = ""
        for n in numer:
            if 1 <= num < 5:
                roman += "I"
            elif 10 <= num < 50:
                roman += "V"
            elif 50 <= num < 100:
                roman += ""
            top = (num // n )
            left = num % n
            num //= n
            print(f"{n},\t{top=},\t{left=}")
        print()



test1 = Solution()
test1.intToRoman(3)
test1.intToRoman(58)
test1.intToRoman(1994)