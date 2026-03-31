class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l = 0
        mp = Counter(s1) #counter builds hashmap auto w/o loop
        mp2 = {}

        for r in range(len(s2)):
            mp2[s2[r]] = 1 + mp2.get(s2[r], 0)

            while r-l+1 > len(s1):
                mp2[s2[l]] -= 1
                if mp2[s2[l]] == 0:
                    del mp2[s2[l]]
                l+=1
            
            if mp == mp2:
                return True
        
        return False

