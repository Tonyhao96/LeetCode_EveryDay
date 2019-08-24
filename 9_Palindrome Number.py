#Low effient but simple
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            x_inverse=int(str(x)[::-1])
            return x==x_inverse

#Brief
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]