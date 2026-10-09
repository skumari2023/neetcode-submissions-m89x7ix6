class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l = 0
        h1 = {}
        h2 = {}
        minLen = float("inf") #make min a high number

        for c in t:
            h2[c] = h2.get(c, 0) + 1

        have = 0
        need = len(h2)
        store = 0

        for r in range(len(s)):
            
            h1[s[r]] = h1.get(s[r], 0) + 1

            if s[r] in h2 and h1[s[r]] == h2[s[r]]:
                have += 1
            
            while have == need:
                
                if (r-l+1) < minLen:
                    minLen = r - l + 1
                    store = l

                h1[s[l]] -= 1 
                #do not delete this bc comparison cannot occur in next step
                
                if s[l] in h2 and h1[s[l]] < h2[s[l]]:
                    have -= 1
                
                l += 1
      
        if minLen == float("inf"): #handle if substring DNE
            return ""
        else:
            return s[store: store + minLen]



