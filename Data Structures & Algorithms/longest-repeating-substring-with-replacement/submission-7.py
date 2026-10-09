class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        curr = {}
        ans = 0

        for r in range(len(s)):
            curr[s[r]] = curr.get(s[r], 0) + 1

            while (r - l + 1) - max(curr.values()) > k:
                if curr[s[l]] == 1:
                    del curr[s[l]]
                else:
                    curr[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans


