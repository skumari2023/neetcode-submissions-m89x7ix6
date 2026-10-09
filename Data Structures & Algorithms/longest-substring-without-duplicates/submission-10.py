class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0 
        curr = ""
        ans = 0

        for r in range(len(s)):
            while s[r] in curr:
                curr = curr[1:]
                l += 1
            curr += s[r]
            ans = max(ans, r - l + 1)
        return ans