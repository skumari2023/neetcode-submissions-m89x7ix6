class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0 
        mp = {}
        maxL = 0

        for r in range(len(s)):
            mp[s[r]] = 1 + mp.get(s[r], 0)
            #window = invalid if more than k replacements required
            while (r-l+1) - max(mp.values()) > k:
                mp[s[l]] -= 1
                if mp[s[l]] == 0:
                    del mp[s[l]]
                l+=1
            maxL = max(maxL, r-l+1)
        return maxL
            
