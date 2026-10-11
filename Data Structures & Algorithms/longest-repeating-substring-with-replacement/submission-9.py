class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0 
        ans = {}
        length = 0

        for r in range(len(s)):
            ans[s[r]] = ans.get(s[r], 0) + 1

            while (r - l + 1) - max(ans.values()) > k:
                if ans[s[l]] == 1:
                    del ans[s[l]]
                else:
                    ans[s[l]] -= 1
                l += 1
            
            length = max(length, r - l + 1)

        return length

        