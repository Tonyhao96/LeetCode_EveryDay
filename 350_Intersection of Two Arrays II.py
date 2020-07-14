#350_Intersection of Two Arrays II

#Hash (Using Counter)
#Time complexity: O(m+n)  Space complexity: O(min(m,n))
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1, counts2 = collections.Counter(
            nums1), collections.Counter(nums2)
        res = counts1 & counts2
        return res.elements()

#Hash (Without Counter)
#Time complexity: O(m+n)  Space complexity: O(min(m,n))
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        res, counts = [], {}
        for i in nums1:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        for i in nums2:
            if i in counts:
                if counts[i] > 0:
                    res.append(i)
                    counts[i] -= 1
        return res

#Sort and Double Pointers
#Time complexity: O(mlogm+nlogn)  Space complexity: O(min(m,n))
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        idx1, idx2, res = 0, 0, []

        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] < nums2[idx2]:
                idx1 += 1
            elif nums1[idx1] > nums2[idx2]:
                idx2 += 1
            else:
                res.append(nums1[idx1])
                idx1 += 1
                idx2 += 1
        return res