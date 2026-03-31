class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #you keep expanding the window and when a freq matches 
        #k then you replace it and get the max array length

        l = 0
        mp = {}
        maxLength = 0
        maxFreq = 0

        for r in range(len(s)):
            mp[s[r]] = 1 + mp.get(s[r], 0)
            maxFreq = max(maxFreq, mp[s[r]])
            while (r-l+1) - maxFreq > k:
                mp[s[l]] -= 1
                l+=1
            maxLength = max(maxLength, r-l+1)
            
        return maxLength 


        
        