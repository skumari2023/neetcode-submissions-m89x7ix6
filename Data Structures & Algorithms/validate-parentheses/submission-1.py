class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        close = { "}":"{", "]":"[", ")":"("}

        for c in s:
            if c in close:
                #stack[-1] checks the previous character added to stack
                if stack and stack[-1] == close[c]:
                    stack.pop() #just calling .pop() removes previous character
                else:
                    return False
            
            else:
                stack.append(c)
        
        return True if not stack else False
        