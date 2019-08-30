#38_Count and Say
class Solution:
    def countAndSay(self, n: int) -> str:
        term='1'
        for i in range(1,n):
            next_term, count, number = '', 1, term[0]
            
            for j in range(1,len(term)):
                if number==term[j]:
                    count+=1
                else:
                    next_term+=str(count)+number
                    number=term[j]
                    count=1
            next_term+=str(count)+number
            term=next_term
        return term