#189_Rotate Array

#Rotate k times
#Time complexity: O(n*k)  Space complexity: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            temp = nums[-1]
            nums[1::] = nums[:-1]
            nums[0] = temp

