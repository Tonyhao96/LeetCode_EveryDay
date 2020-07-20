#3_Longest Substring Without Repeating Characters
#Use Dict
#Time complexity: O(n)  Space complexity: O(k)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, k, sub = 0, -1, {}
        for i, c in enumerate(s):
            if c in sub and sub[c] > k:
                k = sub[c]
                sub[c] = i
            else:
                sub[c] = i
                res = max(res, i - k)
        return res
