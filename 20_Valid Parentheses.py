#20_Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        bracketdict={")": "(", "}": "{", "]": "["}
        stack=[]
        for i in s:
            if i in bracketdict:
                top=stack.pop() if stack else '#'
                
                if bracketdict[i] !=top:
                    return False
            else:
                stack.append(i)
            
        return not stack