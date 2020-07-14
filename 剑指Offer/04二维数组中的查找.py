#面试题04.二维数组中的查找

#From Top Right Number
#Time complexity: O(N+M)  (Number of Rows and Columns)  Space complexity: O(1)
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        i, j = 0, len(matrix[0])-1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True 
            elif matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1 
        return False
    