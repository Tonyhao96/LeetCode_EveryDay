# 67_Add Binary

# Transfer to int
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = int(a, 2)+int(b, 2)
        return bin(result)[2:]

# Recursive
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1')+'0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1], b[0:-1])+'0'
        else:
            return self.addBinary(a[0:-1], b[0:-1])+'1'
