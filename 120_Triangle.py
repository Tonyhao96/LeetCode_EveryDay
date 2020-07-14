#120_Triangle

#Dynamic Programming
#Time complexity: O(n^2)  Space complexity: O(n^2)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0]*n for _ in range(n)]
        f[0][0] = triangle[0][0]

        for i in range(1, n):
            f[i][0] = f[i-1][0] + triangle[i][0]
            for j in range(1, i):
                f[i][j] = min(f[i-1][j], f[i-1][j-1]) + triangle[i][j]
            f[i][i] = f[i-1][i-1] + triangle[i][i]
        return min(f[n-1])

#Dynamic Programming, with Space Optimize
#Time complexity: O(n^2)  Space complexity: O(n)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [0]*n
        f[0] = triangle[0][0]

        for i in range(1, n):
            f[i] = f[i-1] + triangle[i][i]
            for j in range(i-1, 0, -1):
                f[j] = min(f[j], f[j-1]) + triangle[i][j]
            f[0] = f[0] + triangle[i][0]
        return min(f)
