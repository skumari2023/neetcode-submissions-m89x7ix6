class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for c in s:
            
            if c == "[":
                stack.append(c)
            if c == "{":
                stack.append(c)
            if c == "(":
                stack.append(c)
            
            if c == ")" and not stack:
                return False
            if c == "}" and not stack:
                return False
            if c == "]" and not stack:
                return False
           
            if c == ")" and stack[-1] != "(":
                return False
            if c == "}" and stack[-1] != "{":
                return False
            if c == "]" and stack[-1] != "[":
                return False
            
            if c == ")" and stack[-1] == "(":
                stack.pop()
            if c == "}" and stack[-1] == "{":
                stack.pop()
            if c == "]" and stack[-1] == "[":
                stack.pop()
            

        if not stack:
            return True
        else:
            return False