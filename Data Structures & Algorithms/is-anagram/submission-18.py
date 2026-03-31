class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check the char frequencies of both strings 
        #cannot change value is get method for hash maps

        char1 = {}
        char2 = {}

        for c1 in s:
            if c1 in char1:
                char1[c1] += 1
            else:
                char1[c1] = 1
        
        for c2 in t:
            if c2 in char2:
                char2[c2] += 1
            else:
                char2[c2] = 1
        
        if char1 == char2:
            return True
        
        return False 
        