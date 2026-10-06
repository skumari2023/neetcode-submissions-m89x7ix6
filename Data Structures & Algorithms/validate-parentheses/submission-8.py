class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        close = {"}":"{", ")":"(" , "]":"["} #did not grasp this format

        for c in s:
            if c in close:
                if stack and close[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        else: 
            return False
