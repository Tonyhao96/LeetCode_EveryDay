#面试题10-II.青蛙跳台阶问题

#Using Recursive Method  With lRU Cache
#Time complexity: O(n)  Space complexity: O(n)
import functools

class Solution:
    @functools.lru_cache
    def numWays(self, n: int) -> int:
        return (self.numWays(n-1) + self.numWays(n-2)) % 1000000007 if n > 1 else 1


#Using Dynamic Programming
#Time complexity: O(n)  Space complexity: O(n)
class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007