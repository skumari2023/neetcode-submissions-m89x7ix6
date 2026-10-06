class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        h1 = {}
        h2 = {}

        for n in s:
            h1[n] = h1.get(n,0) + 1
        
        for c in t:
            h2[c] = h2.get(c,0) + 1
        
        return h1 == h2

        