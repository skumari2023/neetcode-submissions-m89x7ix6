class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        mp1 = Counter(s)
        mp2 = Counter(t)

        if mp1 == mp2:
            return True
        else:
            return False