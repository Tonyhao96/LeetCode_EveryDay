# 8_String to Integer (atoi)

class Solution:
    def myAtoi(self, str: str) -> int:
        flag = True
        sign, s = 1, 0
        d = {'0':0, '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

        for c in str:
            if c == ' ' and flag:
                continue
            elif c == '-' and flag:
                flag = False
                sign = -1
            elif c == '+' and flag:
                flag = False
            elif c not in d:
                break
            else:
                s = 10*s + d[c]
            flag = False
        result = s * sign
        return min(max(result, -2**31), 2**31 - 1)