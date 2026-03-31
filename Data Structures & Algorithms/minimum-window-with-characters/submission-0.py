class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l = 0
        res = [-1,-1]
        resLen = float("infinity")
        mp = Counter(t)
        window = {}
        have = 0
        need = len(mp)

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in mp and mp[s[r]] == window[s[r]]:
                have+=1
            
            while have == need:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l,r]
                window[s[l]] -= 1
                if s[l] in mp and window[s[l]] < mp[s[l]]:
                    have-=1
                l += 1
            
        l,r = res #unpacks the array 
        if resLen != float("infinity"):
            return s[l:r+1]
        else:
            return ""
        
