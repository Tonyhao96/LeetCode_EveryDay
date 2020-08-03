# 415_Add Strings

#Using dict
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

#Using carry bit
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carry, res = len(num1) - 1, len(num2) - 1, 0, ''
        while i >= 0 or j >= 0:
            a = num1[i] if i >= 0 else '0'
            b = num2[j] if j >= 0 else '0'
            r = ord(a) + ord(b) - 2 * ord('0') + carry
            carry = r // 10
            r = r % 10
            res = chr(r + 48) + res
            i -= 1
            j -= 1
        return '1' + res if carry else res
