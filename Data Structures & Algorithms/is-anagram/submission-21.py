class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sFreq = {}
        tFreq = {}

        for c in s:
            if c in sFreq:
                sFreq[c] += 1
            else:
                sFreq[c] = 1
        
        for ct in t:
            if ct in tFreq:
                tFreq[ct] += 1
            else:
                tFreq[ct] = 1
        
        if sFreq == tFreq:
            return True
        
        return False
        