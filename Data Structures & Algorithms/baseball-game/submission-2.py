class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        output = 0
        val = 0 #need to crete new variable 

        for c in range (len(operations)):

            if operations[c] == "+":
                val = int(stack[-1])+int(stack[-2])
                stack.append(val)
                output+= val
            
            elif operations[c] == "C":
                val = int(stack[-1])
                stack.pop()
                output -= val
            
            elif operations[c] == "D":
                val = int(stack[-1])*2
                stack.append(val)
                output += val

            else:
                val = int(operations[c])
                stack.append(val)
                output += val
            
        
        return output 
            
        
