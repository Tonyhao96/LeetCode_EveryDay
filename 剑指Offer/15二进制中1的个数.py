#面试题15.二进制中1的个数

#Using Bit Computation
#Time complexity: O(logN)  Space complexity: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1 & n
            n >>= 1
        return res

#Using n&(n-1)
#Time complexity: O(n)   Space complexity: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res