class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        zipstr=list(zip(*strs))
        
        for i in zipstr:
            if len(set(i))==1:
                prefix+=i[0]
            else:
                break
        
        return prefix