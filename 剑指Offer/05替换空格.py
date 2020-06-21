#面试题05.替换空格

#Using '+'
#Time complexity: O(N+M)  Space complexity: O(1)
class Solution:
    def replaceSpace(self, s: str) -> str:
        result = ''
        for c in s:
            if c == ' ':
                result = result + '%20'
            else:
                result = result + c
        return result

#Using 'Replace'
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')

##Using 'Join'
class Solution:
    def replaceSpace(self, s: str) -> str:
        result = ''
        for c in s:
            if c == ' ':
                result = ''.join([result, '%20'])
            else:
                result = ''.join([result, c])
        return result

