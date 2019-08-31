#7_Reverse Integer

#Using String Inverted Order Method
#Low effient but simple
class Solution:
    def reverse(self, x: int):
        if x<0 :
            x_reverse=-int(str(-x)[::-1])
        else:
            x_reverse=int(str(x)[::-1])
        if x_reverse>(2**31-1) or x_reverse<-2**31 :
            return 0
        else:
            return x_reverse

#Using Division Method
#Better effient
class Solution:
    def reverse(self, x: int):
        flag=1 if x>=0 else -1
        x=abs(x)
        x_reverse=0
        while x!=0:
            x_reverse=x_reverse*10+x%10
            x=x//10
        if x_reverse>(2**31-1) or x_reverse<-2**31 :
            return 0
        return x_reverse