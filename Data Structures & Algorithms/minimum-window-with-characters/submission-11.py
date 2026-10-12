class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l = 0
        
        start = 0
        ans = float("inf")
        
        hm = {}
        hm2 = {}

        for c in t:
            hm[c] = hm.get(c, 0) + 1

        have = 0
        need = len(hm)

        for r in range(len(s)):

            hm2[s[r]] = hm2.get(s[r], 0) + 1

            if s[r] in hm and hm2[s[r]] == hm[s[r]]:
                have += 1
            
            while have == need:

                if (r-l+1) < ans:
                    ans = r - l + 1
                    start = l

                hm2[s[l]] -= 1
                
                if s[l] in hm and hm2[s[l]] < hm[s[l]]: 
                    #less than bc you can have more but not less
                    have -= 1
                
                l += 1
        
        if ans == float("inf"):
            return ""
        else:
            return s[start : start + ans]
