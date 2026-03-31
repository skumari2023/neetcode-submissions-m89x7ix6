class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0 
        maxL = 0
        set1 = set()

        for r in range(len(s)):

            while s[r] in set1:
                set1.remove(s[l])
                l+=1
            
            set1.add(s[r])

            maxL = max(maxL, r - l + 1)

        return maxL
