# 69_Sqrt(x)

# Binary Search
class Solution:
    def mySqrt(self, x: int) -> int:
        a, b = 0, x
        while a <= b:
            mid = (a+b)//2
            if mid**2 == x:
                return mid
            if mid**2 > x:
                b = mid-1
            else:
                a = mid+1
        return b


# Newton method
class Solution:
    def mySqrt(self, x: int) -> int:
        result = x
        while result**2 > x:
            result = (result**2+x)//(2*result)
        return result
