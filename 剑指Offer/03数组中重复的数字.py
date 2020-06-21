#面试题03.数组中重复的数字

#Sort Method
#Time complexity: O(nlog(n))  Space complexity: O(n)
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        s = sorted(nums)
        for i in range(len(nums)):
            if s[i] == s[i+1]:
                return s[i]

#Hash Dict
#Time complexity: O(n))  Space complexity: O(n)
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            else:
                return i

# Exchange Index   !!! Only valid when list long enough
#Time complexity: O(n))  Space complexity: O(1)
class Solution(object):
    def findRepeatNumber(self, nums):
        for i in range(len(nums)):
            while nums[i]!=i:
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
