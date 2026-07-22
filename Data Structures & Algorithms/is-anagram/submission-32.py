class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hashmap1 = {}
        hashmap2 = {}

        for charS in s:
            hashmap1[charS] = hashmap1.get(charS,0) + 1

        for charT in t:
            hashmap2[charT] = hashmap2.get(charT,0) + 1
        
        if hashmap1 == hashmap2:
            return True
        else:
            return False

