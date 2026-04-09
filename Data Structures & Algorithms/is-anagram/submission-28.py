class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sFreq = Counter(s)
        tFreq = Counter(t)

        if sFreq == tFreq:
            return True
        else:
            return False