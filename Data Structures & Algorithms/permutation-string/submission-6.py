class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0 
        mp = Counter(s1)
        window = {}

        for r in range(len(s2)):
            window[s2[r]] = 1 + window.get(s2[r], 0)

            while (r-l+1) > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l+=1
           
            if mp == window:
                return True
        
        return False
        