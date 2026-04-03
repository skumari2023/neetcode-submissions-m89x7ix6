class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0 
        mp = {}
        maxL = 0

        for r in range(len(s)):
            mp[s[r]] = 1 + mp.get(s[r], 0)
            while mp[s[r]] > 1:
                mp[s[l]] -= 1
                l+=1
            maxL = max(maxL, r-l+1)
        return maxL
