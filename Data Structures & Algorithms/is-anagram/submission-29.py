class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sFreq = {}
        tFreq = {}

        for x in s:
            sFreq[x] = 1 + sFreq.get(x, 0)
        
        for y in t:
            tFreq[y] = 1 + tFreq.get(y,0)
        
        if sFreq == tFreq:
            return True
        else:
            return False