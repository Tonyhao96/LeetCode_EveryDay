# 415_Add Strings
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        dict = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
                "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}

        def toint(s):
            res = 0
            for i in range(len(s)):
                res *= 10
                res += dict[s[i]]
            return res
        return str(toint(num1)+toint(num2))
