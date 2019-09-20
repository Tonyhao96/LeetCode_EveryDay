#290_Word Pattern
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        strlist=str.split()
        if len(strlist)!=len(pattern):
            return False
        return len(set(strlist))==len(set(pattern))==len(set(zip(pattern,strlist)))