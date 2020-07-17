#35_Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return i+1

# Using Bisection Method
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        if target > nums[right]:
            return len(nums)
        while left < right:
            mid = ((right - left) >> 1) + left
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left
