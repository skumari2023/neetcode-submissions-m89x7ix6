class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hash1 = {}
        hash2 = {}

        if len(s) != len(t):
            return False
        
        for c1 in s:
            hash1[c1] = hash1.get(c1, 1) + 1
        
        for c2 in t:
            hash2[c2] = hash2.get(c2, 1) + 1
        
        return hash1 == hash2
        