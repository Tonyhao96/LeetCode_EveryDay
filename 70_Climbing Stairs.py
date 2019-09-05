# 70_Climbing Stairs

# One line Fibonacci
class Solution:
    def climbStairs(self, n: int) -> int:
        return int(((1 + 5**.5) / 2) ** -~n / 5**.5 + .5)
        # -~n, that's just short for (n+1)

# Iterative Fibonacci
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(1, n):
            a, b = b, a+b
        return b
