#189_Rotate Array

#Using Hash
#Time complexity: O(n)  Space complexity: O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            temp = nums[-1]
            nums[1::] = nums[:-1]
            nums[0] = temp