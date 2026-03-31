class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0
        lenS = len(s1) 
        counter1 = Counter(s1)
        counter2 = {}

        for right in range(len(s2)):

            if counter1 == counter2:
                return True
            
            counter2[s2[right]] = counter2.get(s2[right], 0) + 1
            
            if right-left + 1 >= lenS and counter1 != counter2:
                counter2[s2[left]] -= 1
                
                if counter2[s2[left]] == 0:
                    del counter2[s2[left]]
            
                left += 1

        return counter1 == counter2
