class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        stringS = {}
        stringT = {}

        for input1 in s:
            if input1 in stringS:
                stringS[input1] += 1
            else:
                stringS[input1] = 1
        
        for input2 in t:
            if input2 in stringT:
                stringT[input2] += 1
            else:
                stringT[input2] = 1
        
        if stringT == stringS:
            return True
        
        return False

