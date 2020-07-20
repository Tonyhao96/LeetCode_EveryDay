#991_Broken Calculator

#Reverse, Y divide by 2 or add 1, thus odd: +1, even: /2
#Time complexity: O(log(Y))  Space complexity: O(1)
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        res = 0
        while Y > X:
            if Y % 2:
                Y += 1
            else:
                Y = Y // 2
            res += 1
        return res + X - Y