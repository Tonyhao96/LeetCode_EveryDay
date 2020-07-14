#面试题10-I.斐波那契数列

#Using Recursive Method  With lRU Cache
#Time complexity: O(n)  Space complexity: O(n)
import functools

class Solution:
    @functools.lru_cache
    def fib(self, n: int) -> int:
        return n if n < 2 else (self.fib(n-1) + self.fib(n-2)) % 1000000007


#Using Dynamic Programming
#Time complexity: O(n)  Space complexity: O(n)
class Solution:
    def fib(self, n: int) -> int:
        if n < 2 : return n
        num = [0 for _ in range(n+1)]
        num[1] = 1
        for i in range(2, n+1):
            num[i] = num[i-1] + num[i-2]
        return num[-1] % 1000000007
