class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0 
        ans = ""
        curr = {}
        length = 0

        for r in range(len(s)):

            curr[s[r]] = curr.get(s[r], 0) + 1

            while curr[s[r]] > 1:
                if curr[s[l]] == 1:
                    del curr[s[l]]
                else:
                    curr[s[l]] -= 1
                l += 1
            
            length = max(length, r - l + 1)

        return length

            