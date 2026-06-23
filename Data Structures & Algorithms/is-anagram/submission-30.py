class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hash1 = {}
        hash2 = {}

        if len(s) != len(t):
            return False
        
        for char1 in s:
            hash1[char1] = hash1.get(char1, 0) + 1
        
        for char2 in t:
            hash2[char2] = hash2.get(char2, 0) + 1
        
        return hash1 == hash2