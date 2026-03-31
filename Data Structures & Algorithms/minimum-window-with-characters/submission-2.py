class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l = 0

        mp = Counter(t)
        window = {}

        need = len(mp)
        have = 0

        res = [-1,-1]
        resLen = float("infinity")

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in mp and mp[s[r]] == window[s[r]]:
                have += 1
            
            while need == have:
                if r-l+1 < resLen:
                    res = [l,r]
                    resLen = r-l+1
                window[s[l]] -= 1
                if s[l] in mp and window[s[l]] < mp[s[l]]:
                    have -=1
                l+=1
        
        l,r = res
        if resLen != float("infinity"):
            return s[l:r+1]
        else:
            return ""


