# 88_Merge Sorted Array

# Using sort
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2[:n]
        nums1.sort()


# Using deque
from collections import deque
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        q1 = deque(nums1[:m])
        q2 = deque(nums2[:n])
        nums1[:] = []
        while q1 and q2:
            if q1[0] <= q2[0]:
                nums1.append(q1.popleft())
            else:
                nums1.append(q2.popleft())
        nums1 += q1 or q2
