#96_Unique Binary Search Trees

#Dynamic Programming
#Time complexity: O(n^2)  Space complexity: O(n)
class Solution:
    def numTrees(self, n: int) -> int:
        F = [0] * (n + 1)
        F[0], F[1] = 1, 1

        for i in range(2, n+1):
            for j in range(i):
                F[i] += F[j] * F[i-j-1]
        return F[n]

#Catalan Number
#Time complexity: O(n)  Space complexity: O(1)
class Solution:
    def numTrees(self, n: int) -> int:
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)