class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #input: two strings s and t 
        #output: true if both strings have the same character freq
        #else false

        freq1 = 26 * [0]
        freq2 = 26 * [0]

        for c in s:
            freq1[ord(c) - 97] += 1

        for ch in t:
            freq2[ord(ch) - 97] += 1
        
        if freq1 == freq2:
            return True
        
        return False