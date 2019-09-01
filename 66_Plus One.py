#66_Plus One

#One line
class Solution:
   def plusOne(self, digits: List[int]) -> List[int]:
       return list(map(int, str(int(''.join(map(str, digits)))+1)))


#Normal Approach
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value=0
        for i in digits:
            value=value*10
            value+=i
        return list(str(value+1))