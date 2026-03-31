class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        l = 0 
        maxL = 0
        mp = {}

        for r in range(len(s)):
            
            mp[s[r]] = 1 + mp.get(s[r], 0)

            while (r-l+1) - max(mp.values()) > k:
                mp[s[l]] -= 1
                if mp[s[l]] == 0:
                    del mp[s[l]]
                l+=1
            #window = invalid if number or replacements > k

            maxL = max(maxL, r - l + 1)
        
        return maxL