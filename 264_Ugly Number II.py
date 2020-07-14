#264_Ugly Number II
#Use Dynamic Promgramming
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2, i3, i5 = 0, 0, 0
        for _ in range(n-1):
            u = min(nums[i2]*2, nums[i3]*3, nums[i5]*5)
            nums.append(u)

            while nums[i2]*2 <= u:
                i2 += 1
            while nums[i3]*3 <= u:
                i3 += 1
            while nums[i5]*5 <= u:
                i5 += 1
        return nums[n-1]
