#58_Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        inverse=s[::-1]
        for i in range(len(s)):
            if inverse[i]==' ':
                return i
        return len(s)