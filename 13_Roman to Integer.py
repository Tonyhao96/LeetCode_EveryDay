class Solution:
    def romanToInt(self, s: str) -> int:
        result=0
        maxflag=0
        romandict={"I": 1, "V": 5,"X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
        
        for i in reversed(s):
            temp=romandict[i]
            if temp>=maxflag:
                result+=temp
                maxflag=temp
            else :
                result-=temp
        return result