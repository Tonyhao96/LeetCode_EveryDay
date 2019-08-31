#53_Maximum Subarray

#Dynamic Programming
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        listsum=[0]*len(nums)
        listsum[0]=nums[0]
        
        for i in range(1,len(nums)):
            listsum[i]=max(nums[i],nums[i]+listsum[i-1])
        return max(listsum)
        
#Dynamic Programming 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:        
        for i in range(1,len(nums)):
            nums[i]=max(nums[i],nums[i]+nums[i-1])
        return max(nums)

#Using itertools
from itertools import accumulate
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return max(accumulate(nums, lambda x, y: max(y, x+y) ))