# 383_Ransom Note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            if ransomNote[i] not in magazine:
                return False
            magazine = magazine.replace(ransomNote[i], '', 1)
        return True
