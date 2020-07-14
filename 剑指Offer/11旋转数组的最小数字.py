#面试题11.旋转数组的最小数字

#Using Direct Search
#Time complexity: O(n)  Space complexity: O(1)
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                return numbers[i+1]
        return numbers[0]

#Using Dichotomy Method
#Time complexity: O(logN) (Worst situation: O(N))  Space complexity: O(1)
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                j -= 1
        return numbers[i]
        