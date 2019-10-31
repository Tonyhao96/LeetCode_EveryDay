# 420_Strong Password Checker
import math


class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        miss_type, p, length = 3, 2, len(s)
        a, b, change = 0, 0, 0
        # Miss type check
        if any('a' <= c <= 'z' for c in s):
            miss_type -= 1
        if any('A' <= c <= 'Z' for c in s):
            miss_type -= 1
        if any(c.isdigit() for c in s):
            miss_type -= 1

        # Repeat check
        while p < length:
            if s[p] == s[p-1] == s[p-2]:
                l = 2
                while p < length and s[p] == s[p-1]:
                    l += 1
                    p += 1
                change += l//3
                if l % 3 == 0:
                    a += 1
                elif l % 3 == 1:
                    b += 1
            else:
                p += 1

        # Length check
        if length < 6:
            return max(miss_type, 6 - length)
        elif length <= 20:
            return max(miss_type, change)
        else:
            delete = length - 20
            change -= min(delete, a)
            change -= min(max(delete-a, 0), b*2) / 2
            change -= max(delete - a-2*b, 0)/3

            return delete + math.ceil(max(miss_type, change))
