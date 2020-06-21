#154_Find Minimum in Rotated Sorted Array II

#Using Direct Search
#Time complexity: O(n)  Space complexity: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]

#Using Dichotomy Method
#Time complexity: O(logN) (Worst situation: O(N))  Space complexity: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            m = (i + j) // 2
            if nums[m] > nums[j]:
                i = m + 1
            elif nums[m] < nums[j]:
                j = m
            else:
                j -= 1
        return nums[i]